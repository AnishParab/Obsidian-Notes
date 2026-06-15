# LazyVim JS Setup

Install via Mason (`:MasonInstall`):
```
eslint-lsp
prettierd
typescript-language-server
tailwindcss-language-server
emmet-ls
js-debug-adapter
```

> **Gotcha** — LazyVim's typescript extra auto-installs `typescript-language-server` and configures eslint. Don't double-configure or you'll get duplicate LSP clients.

---
# `~/.config/nvim/lua/plugins/lang-js.lua`

```lua
return {
  -- TypeScript/JS LSP
  { "nvim-treesitter/nvim-treesitter",
    opts = function(_, opts)
      vim.list_extend(opts.ensure_installed, {
        "javascript", "typescript", "tsx", "html", "css", "json"
      })
    end
  },

  -- LazyVim JS/TS extra (handles tsserver, eslint automatically)
  { import = "lazyvim.plugins.extras.lang.typescript" },

  -- Tailwind
  { import = "lazyvim.plugins.extras.lang.tailwind" },

  -- Formatting
  {
    "stevearc/conform.nvim",
    opts = {
      formatters_by_ft = {
        javascript      = { "prettierd" },
        typescript      = { "prettierd" },
        javascriptreact = { "prettierd" },
        typescriptreact = { "prettierd" },
        css             = { "prettierd" },
        html            = { "prettierd" },
        json            = { "prettierd" },
      }
    }
  },
}
```

---
# Enable LazyVim extras in `~/.config/nvim/lua/config/lazy.lua`:

```lua
{ import = "lazyvim.plugins.extras.lang.typescript" },
{ import = "lazyvim.plugins.extras.lang.tailwind" },
```

---
