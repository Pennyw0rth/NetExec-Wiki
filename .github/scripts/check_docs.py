import os
import re
import argparse
import subprocess
import datetime

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.columns import Columns
    from rich.tree import Tree
    from rich.table import Table
    from rich.text import Text
    from rich import box
except ImportError:
    print("The 'rich' library is required for formatted output. Please run: pip install rich")
    exit(1)

console = Console()

def get_module_sync(wiki_dir, code_dir):
    modules_dir = os.path.join(code_dir, 'nxc', 'modules')
    if not os.path.isdir(modules_dir):
        return set(), set()
    code_modules = {f[:-3] for f in os.listdir(modules_dir) if f.endswith('.py') and f not in ['__init__.py', 'example_module.py']}
    
    found_modules = set()
    wiki_modules = set()
    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if f.endswith('.md'):
                with open(os.path.join(root, f), 'r', encoding='utf-8') as md:
                    content = md.read()
                    for cm in code_modules:
                        if re.search(r'\b' + re.escape(cm) + r'\b', content):
                            found_modules.add(cm)
                    for match in re.finditer(r'(?:-M|--module)\s+([a-zA-Z0-9_\-]+)', content):
                        wiki_modules.add(match.group(1))
                        
    return code_modules - found_modules, wiki_modules - code_modules

def get_flag_sync(wiki_dir, code_dir):
    protocols_dir = os.path.join(code_dir, 'nxc', 'protocols')
    flags_by_protocol = {}
    all_code_flags = set(['-h', '--help'])
    
    cli_path = os.path.join(code_dir, 'nxc', 'cli.py')
    if os.path.isfile(cli_path):
        with open(cli_path, 'r', encoding='utf-8') as f:
            for arg in re.findall(r'\.add_argument\([^)]+\)', f.read()):
                for match in re.findall(r'[\'"](--[a-zA-Z0-9_\-]+|-[a-zA-Z0-9])[\'"]', arg):
                    all_code_flags.add(match)

    for proto in os.listdir(protocols_dir):
        proto_args_path = os.path.join(protocols_dir, proto, 'proto_args.py')
        if os.path.isfile(proto_args_path):
            with open(proto_args_path, 'r', encoding='utf-8') as f:
                args = re.findall(r'\.add_argument\([^)]+\)', f.read())
                flags = set()
                for arg in args:
                    for match in re.findall(r'[\'"](--[a-zA-Z0-9_\-]+|-[a-zA-Z0-9])[\'"]', arg):
                        flags.add(match)
                        all_code_flags.add(match)
                if flags:
                    flags_by_protocol[proto] = flags

    missing_flags_by_proto = {}
    for proto, flags in flags_by_protocol.items():
        proto_wiki_dir = os.path.join(wiki_dir, f"{proto}-protocol")
        if not os.path.isdir(proto_wiki_dir):    
            continue
        found_flags = set()
        for root, dirs, files in os.walk(proto_wiki_dir):
            for f in files:
                if f.endswith('.md'):
                    with open(os.path.join(root, f), 'r', encoding='utf-8') as md:
                        content = md.read()
                        for flag in flags:
                            if flag in content:
                                found_flags.add(flag)
        missing = {m for m in (flags - found_flags) if m not in ['-h', '--help']}
        if missing:
            missing_flags_by_proto[proto] = missing
            
    wiki_flags = set()
    for root, dirs, files in os.walk(wiki_dir):
        if '.git' in root or '.gitbook' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                with open(os.path.join(root, f), 'r', encoding='utf-8') as md:
                    for line in md.read().split('\n'):
                        line = line.strip()
                        if line.startswith('nxc ') or line.startswith('cme '):
                            for match in re.finditer(r'(?:\s|^)(--[a-zA-Z0-9_\-]+|-[a-zA-Z0-9])(?:\s|$|=)', line):
                                wiki_flags.add(match.group(1))
                                
    deprecated_flags = {f for f in (wiki_flags - all_code_flags) if not f.startswith('--http')}
    return missing_flags_by_proto, deprecated_flags

def get_outdated_tags(wiki_dir):
    cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=180)
    outdated = []
    
    for root, dirs, files in os.walk(wiki_dir):
        if '.git' in root or '.gitbook' in root: continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                with open(filepath, 'r', encoding='utf-8') as md:
                    lines = md.readlines()
                if any('🆕' in line for line in lines):
                    cwd = os.getcwd()
                    os.chdir(wiki_dir)
                    try:
                        rel_path = os.path.relpath(filepath, wiki_dir).replace('\\', '/')
                        blame_out = subprocess.check_output(['git', 'blame', '--line-porcelain', rel_path]).decode('utf-8')
                        blame_lines = blame_out.split('\n')
                        current_committer_time = None
                        
                        for bl in blame_lines:
                            if bl.startswith('committer-time '):
                                current_committer_time = int(bl.split()[1])
                            elif bl.startswith('\t'):
                                current_source_line = bl[1:]
                                if '🆕' in current_source_line and current_committer_time:
                                    dt = datetime.datetime.fromtimestamp(current_committer_time, tz=datetime.timezone.utc)
                                    if dt < cutoff_date:
                                        outdated.append((rel_path, dt.strftime('%Y-%m-%d'), current_source_line.strip()[:60] + "..."))
                    except Exception:
                        pass
                    finally:
                        os.chdir(cwd)
    return outdated

def has_new_tag_in_docs(term, wiki_dir):
    for root, dirs, files in os.walk(wiki_dir):
        if '.git' in root or '.gitbook' in root: continue
        for f in files:
            if f.endswith('.md') and f != "SUMMARY.md":
                with open(os.path.join(root, f), 'r', encoding='utf-8') as md:
                    content = md.read()
                    if re.search(r'\b' + re.escape(term) + r'\b', content) or term in content:
                        if '🆕' in content: return True
    return False

def get_missing_new_tags(wiki_dir, code_dir):
    cutoff_time = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=180)).timestamp()
    modules_dir = os.path.join(code_dir, 'nxc', 'modules')
    recent_modules = []
    
    cwd = os.getcwd()
    os.chdir(code_dir)
    try:
        if os.path.isdir(modules_dir):
            for root, dirs, files in os.walk(modules_dir):
                for f in files:
                    if f.endswith('.py') and f not in ['__init__.py', 'example_module.py']:
                        mod_path = os.path.relpath(os.path.join(root, f), code_dir).replace('\\', '/')
                        try:
                            out = subprocess.check_output(['git', 'log', '--diff-filter=A', '-n', '1', '--format=%ct', '--', mod_path]).decode('utf-8').strip()
                            if out and int(out) > cutoff_time:
                                recent_modules.append(f[:-3])
                        except Exception: pass
    finally:
        os.chdir(cwd)
        
    protocols_dir = os.path.join(code_dir, 'nxc', 'protocols')
    recent_flags = {}
    os.chdir(code_dir)
    try:
        if os.path.isdir(protocols_dir):
            for proto in os.listdir(protocols_dir):
                proto_args_path = os.path.join(protocols_dir, proto, 'proto_args.py')
                if not os.path.isfile(proto_args_path): continue
                try:
                    rel_path = os.path.relpath(proto_args_path, code_dir).replace('\\', '/')
                    blame_lines = subprocess.check_output(['git', 'blame', '--line-porcelain', rel_path]).decode('utf-8').split('\n')
                    current_committer_time = None
                    for bl in blame_lines:
                        if bl.startswith('committer-time '):
                            current_committer_time = int(bl.split()[1])
                        elif bl.startswith('\t'):
                            if current_committer_time and current_committer_time > cutoff_time and '.add_argument' in bl[1:]:
                                for match in re.findall(r'[\'"](--[a-zA-Z0-9_\-]+|-[a-zA-Z0-9])[\'"]', bl[1:]):
                                    if match not in ['-h', '--help']:
                                        recent_flags.setdefault(proto, set()).add(match)
                except Exception: pass
    finally:
        os.chdir(cwd)

    missing_tag_mods = [m for m in recent_modules if not has_new_tag_in_docs(m, wiki_dir)]
    missing_tag_flags = {}
    for proto, flags in recent_flags.items():
        missing = [f for f in flags if not has_new_tag_in_docs(f, wiki_dir)]
        if missing:
            missing_tag_flags[proto] = missing
            
    return missing_tag_mods, missing_tag_flags

def render_report(wiki_dir, code_dir):
    console.print()
    console.rule("[bold bright_yellow]NetExec Documentation Sync Report[/bold bright_yellow]", style="bright_yellow")
    console.print(f"[dim]Wiki Directory: [white]{wiki_dir}[/white][/dim]", justify="center")
    console.print(f"[dim]Code Directory: [white]{code_dir}[/white][/dim]", justify="center")
    console.print()
    
    with console.status("[bold cyan]Analyzing Codebase vs Wiki git history (this takes a few seconds)...", spinner="dots"):
        missing_modules, deprecated_modules = get_module_sync(wiki_dir, code_dir)
        missing_flags_by_proto, deprecated_flags = get_flag_sync(wiki_dir, code_dir)
        outdated_tags = get_outdated_tags(wiki_dir)
        missing_tag_mods, missing_tag_flags = get_missing_new_tags(wiki_dir, code_dir)

    # 1. New Missing Items (Green)
    console.print("[bold bright_yellow]1. Missing Documentation (Required Additions)[/bold bright_yellow]")
    if missing_modules:
        texts = [Text(f"• {m}", style="green") for m in sorted(missing_modules)]
        console.print(Panel(Columns(texts, equal=True, expand=True), title="[bold green]New Modules (Add to Wiki)[/bold green]", border_style="green"))
    
    if missing_flags_by_proto:
        tree = Tree("", hide_root=True)
        for proto, flags in sorted(missing_flags_by_proto.items()):
            p_node = tree.add(f"[bold cyan]{proto}[/bold cyan] protocol")
            p_node.add(Columns([Text(f"• {f}", style="green") for f in sorted(flags)], equal=True, expand=True))
        console.print(Panel(tree, title="[bold green]New Flags (Add to Wiki)[/bold green]", border_style="green"))
        
    if not missing_modules and not missing_flags_by_proto:
        console.print("  [green]✔ Everything is fully documented![/green]\n")
    else:
        console.print()

    # 2. Unknown / Deprecated Items (Yellow)
    console.print("[bold bright_yellow]2. Unknown / Deprecated References (Required Removals)[/bold bright_yellow]")
    if deprecated_modules:
        texts = [Text(f"✗ {m}", style="yellow") for m in sorted(deprecated_modules)]
        console.print(Panel(Columns(texts, equal=True, expand=True), title="[bold yellow]Deprecated/Typo Modules found in Wiki[/bold yellow]", border_style="yellow"))
        
    if deprecated_flags:
        texts = [Text(f"✗ {f}", style="yellow") for f in sorted(deprecated_flags)]
        console.print(Panel(Columns(texts, equal=True, expand=True), title="[bold yellow]Unknown/Removed Flags found in Wiki Examples[/bold yellow]", border_style="yellow"))
        
    if not deprecated_modules and not deprecated_flags:
        console.print("  [green]✔ No bad references found![/green]\n")
    else:
        console.print()

    # 3. New Features Missing 🆕 Tags (Green)
    console.print("[bold bright_yellow]3. Recent Additions (< 6 Months) Missing 🆕 Tags[/bold bright_yellow]")
    if missing_tag_mods:
        texts = [Text(f"★ {m}", style="green") for m in sorted(missing_tag_mods)]
        console.print(Panel(Columns(texts, equal=True, expand=True), title="[bold green]Recent Modules Without 🆕 Tag[/bold green]", border_style="green"))
        
    if missing_tag_flags:
        tree = Tree("", hide_root=True)
        for proto, flags in sorted(missing_tag_flags.items()):
            p_node = tree.add(f"[bold cyan]{proto}[/bold cyan] protocol")
            p_node.add(Columns([Text(f"★ {f}", style="green") for f in sorted(flags)], equal=True, expand=True))
        console.print(Panel(tree, title="[bold green]Recent Flags Without 🆕 Tag[/bold green]", border_style="green"))

    if not missing_tag_mods and not missing_tag_flags:
        console.print("  [green]✔ All recent items are properly tagged![/green]\n")
    else:
        console.print()

    # 4. Outdated Tags (Red)
    console.print("[bold bright_yellow]4. Outdated Tags (> 6 Months)[/bold bright_yellow]")
    if outdated_tags:
        table = Table(box=box.ROUNDED, border_style="red", header_style="bright_yellow", expand=True)
        table.add_column("File Path", style="")
        table.add_column("Date", justify="center", style="")
        table.add_column("Outdated Text Excerpt", style="red")
        for path, dt, text in outdated_tags:
            table.add_row(path, dt, text)
        console.print(table)
    else:
        console.print("  [green]✔ No old tags found![/green]\n")
        
    console.rule("[bold bright_yellow]Check Complete[/bold bright_yellow]", style="bright_yellow")
    console.print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='NetExec Documentation Sync Checker')
    parser.add_argument('--wiki-dir', default='.', help='Path to NetExec-Wiki directory')
    parser.add_argument('--code-dir', default='../NetExec', help='Path to NetExec codebase directory')
    args = parser.parse_args()
    
    render_report(os.path.abspath(args.wiki_dir), os.path.abspath(args.code_dir))
