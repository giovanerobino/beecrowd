# 📚 Guia Completo de Git

Este guia contém os comandos essenciais para gerenciar seu repositório Git, incluindo como puxar (pull) e empurrar (push) alterações.

## 🚀 Comandos Básicos

### Verificar Status
```bash
git status
```
Mostra o estado atual do repositório (arquivos modificados, adicionados, etc.)

### Adicionar Arquivos
```bash
# Adicionar um arquivo específico
git add arquivo.py

# Adicionar todos os arquivos modificados
git add .

# Adicionar todos os arquivos de uma pasta
git add pasta/
```

### Fazer Commit
```bash
# Commit com mensagem
git commit -m "Descrição das alterações"

# Commit adicionando arquivos automaticamente
git commit -am "Mensagem do commit"
```

## 📤 Enviando Alterações (Push)

### Push Básico
```bash
# Enviar para a branch main
git push origin main

# Primeira vez (definir upstream)
git push -u origin main
```

### Processo Completo para Enviar Alterações
```bash
# 1. Verificar status
git status

# 2. Adicionar arquivos modificados
git add .

# 3. Fazer commit
git commit -m "Descrição das alterações"

# 4. Enviar para o GitHub
git push origin main
```

## 📥 Recebendo Alterações (Pull)

### Pull Básico
```bash
# Baixar e aplicar alterações do repositório remoto
git pull origin main
```

### Verificar Alterações Antes do Pull
```bash
# Buscar informações do remoto sem aplicar
git fetch origin

# Ver commits que estão no remoto mas não no local
git log HEAD..origin/main --oneline

# Ver diferenças
git diff HEAD origin/main
```

### Processo Seguro para Pull
```bash
# 1. Verificar se há alterações locais não commitadas
git status

# 2. Se houver alterações, fazer commit ou stash
git stash  # (salva temporariamente)

# 3. Fazer pull
git pull origin main

# 4. Restaurar alterações salvas (se usou stash)
git stash pop
```

## 🔧 Resolvendo Conflitos

### Quando há Conflito no Pull
```bash
# 1. Fazer pull (pode gerar conflito)
git pull origin main

# 2. Editar arquivos em conflito manualmente
# (remover marcadores <<<<<<<, =======, >>>>>>>)

# 3. Adicionar arquivos resolvidos
git add arquivo_resolvido.py

# 4. Finalizar merge
git commit -m "Resolve merge conflict"

# 5. Enviar resultado
git push origin main
```

## 📊 Comandos de Visualização

### Ver Histórico
```bash
# Histórico simples
git log --oneline

# Últimos 5 commits
git log --oneline -5

# Histórico detalhado
git log

# Ver diferenças de um commit
git show commit_hash
```

### Ver Diferenças
```bash
# Diferenças não commitadas
git diff

# Diferenças entre commits
git diff commit1 commit2

# Diferenças de um arquivo específico
git diff arquivo.py
```

## 🌿 Trabalhando com Branches

### Criar e Gerenciar Branches
```bash
# Ver branches
git branch

# Criar nova branch
git branch nova-feature

# Mudar para branch
git checkout nova-feature

# Criar e mudar para nova branch
git checkout -b nova-feature

# Fazer merge de branch
git checkout main
git merge nova-feature

# Deletar branch
git branch -d nova-feature
```

## ⚙️ Configuração Inicial

### Configurar Git (primeira vez)
```bash
# Configurar nome e email
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"

# Ver configurações
git config --list
```

### Conectar Repositório Local ao GitHub
```bash
# Inicializar repositório
git init

# Adicionar remote
git remote add origin https://github.com/usuario/repositorio.git

# Verificar remotes
git remote -v
```

## 🆘 Comandos de Emergência

### Desfazer Alterações
```bash
# Desfazer alterações não commitadas em um arquivo
git checkout -- arquivo.py

# Desfazer todas as alterações não commitadas
git reset --hard HEAD

# Desfazer último commit (mantendo alterações)
git reset --soft HEAD~1

# Desfazer último commit (perdendo alterações)
git reset --hard HEAD~1
```

### Salvar Trabalho Temporariamente
```bash
# Salvar alterações temporariamente
git stash

# Ver stashes salvos
git stash list

# Restaurar último stash
git stash pop

# Restaurar stash específico
git stash apply stash@{0}
```

## 📋 Fluxo de Trabalho Recomendado

### Ao Começar a Trabalhar
```bash
# 1. Sempre puxar últimas alterações
git pull origin main

# 2. Verificar status
git status

# 3. Começar a programar...
```

### Ao Finalizar Trabalho
```bash
# 1. Verificar o que foi alterado
git status

# 2. Adicionar arquivos
git add .

# 3. Fazer commit
git commit -m "Adiciona funcionalidade X"

# 4. Enviar para GitHub
git push origin main
```

### Trabalhando em Equipe
```bash
# 1. Criar branch para nova feature
git checkout -b minha-feature

# 2. Trabalhar normalmente
git add .
git commit -m "Implementa nova feature"

# 3. Enviar branch
git push origin minha-feature

# 4. Criar Pull Request no GitHub
# 5. Após aprovação, fazer merge
```

## 🔍 Comandos Úteis

### Verificar Diferenças Específicas
```bash
# Ver arquivos modificados
git diff --name-only

# Ver estatísticas de alterações
git diff --stat

# Ver alterações de uma linha específica
git blame arquivo.py
```

### Limpar Repositório
```bash
# Remover arquivos não rastreados
git clean -f

# Remover pastas não rastreadas
git clean -fd

# Ver o que seria removido (sem remover)
git clean -n
```

## ⚠️ Dicas Importantes

1. **Sempre fazer pull antes de push** - Evita conflitos
2. **Fazer commits pequenos e frequentes** - Facilita o controle
3. **Usar mensagens descritivas** - Ajuda a entender o histórico
4. **Não fazer push de arquivos sensíveis** - Use .gitignore
5. **Fazer backup regularmente** - Git não substitui backup completo

## 📁 Arquivo .gitignore

Crie um arquivo `.gitignore` para ignorar arquivos desnecessários:

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Sistema
.DS_Store
Thumbs.db

# Logs
*.log

# Arquivos temporários
*.tmp
*.temp
```

---

**💡 Lembre-se:** O Git é uma ferramenta poderosa, mas com grandes poderes vêm grandes responsabilidades. Sempre teste comandos destrutivos em repositórios de teste primeiro!

**🔗 Links Úteis:**
- [Documentação oficial do Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
