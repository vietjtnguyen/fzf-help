# Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Improvements](#improvements)

# Introduction
`fzf-help` is an `fzf` extension that allows you to select one of the command
line options of a given command. The options are retrieved from the command its
`--help` documentation, which is displayed in a preview window. Both zsh and
bash are supported. Tested on Linux, but should work on MacOS as well.

![demo](./demo.gif)

# Installation
Ensure that you have the following tools installed:
- [fzf](https://github.com/junegunn/fzf)
- [bat](https://www.github.com/sharkdp/bat)
- [ag](https://www.github.com/ggreer/the_silver_searcher)

## zsh
Run the following command to install fzf-help in the zsh plugin directory
at `/usr/share/zsh/plugins`.
```bash
tmp_dir=$(mktemp -d);
git clone https://github.com/BartSte/fzf-help.git $tmp_dir;
$tmp_dir/install;
rm -rf $tmp_dir;
```

After installation, add the following line to your `.zshrc` file:
```bash
source /usr/share/zsh/plugins/fzf-help/fzf-help.zsh
zle -N fzf-help-widget
bindkey "^A" fzf-help-widget
```
which will bind the `fzf-help-widget` to the `ctrl-a`, which you should trigger
after typing the command you want to get help for.

## bash
Run the following command to install `fzf-help` in the bash plugin directory
at `/usr/share/fzf-help`.
```bash
tmp_dir=$(mktemp -d);
git clone https://github.com/BartSte/fzf-help.git $tmp_dir;
$tmp_dir/install --bash;
rm -rf $tmp_dir;
```

After installation, you can add the following line to your `.bashrc` file:
```bash
source /usr/share/zsh/plugins/fzf-help/fzf-help.bash
bind -x '"\C-a": fzf-help-widget'
```

# Configuration
The following environment variables can be set to configure the behaviour of
`fzf-help`:
- `FZF_HELP_OPTS`: options to pass to `fzf` when selecting the command to get
  help for. Defaults to:
  ```bash
  FZF_HELP_OPTS="--preview-window=right,75%,wrap --height 80% "
  FZF_HELP_OPTS+="--bind ctrl-a:change-preview-window(down,75%,nowrap|right,75%,nowrap)"
  ```
- `CLI_OPTIONS_REGEX`: regex to match the command line options in the `--help`
  documentation. Check the `cli_options` command for the default value.

- `HELP_MESSAGE_CMD`: controls which command is used to retrieve the command
  line options. Here, the `$cmd` variable is the command to get the options for.
  Defaults to `$cmd --help`. You can use `man -P cat $cmd` if you want to use the
  man page instead of the `--help` documentation.

# Usage
As the demo shows, you can use `fzf-help` by typing `ctrl-a` after typing the
command you want to get help for. This will open `fzf` with a list of options
and the `--help` documentation in the preview window. You can press `ctrl-a`
again to toggle the preview window to the bottom or the right of the widget.
This is usefull when you do not like page wrapping.

# Troubleshooting
If you encounter any issues, please report them on the issue tracker at:
[fzf-help issues](https://github.com/BartSte/fzf-help/issues). 

Please note that `fzf-help` is tested on Linux only.

## Contributing
Contributions are welcome! Please see [CONTRIBUTING](./CONTRIBUTING.md) for
more information.

# License
Distributed under the [MIT License](./LICENCE).
