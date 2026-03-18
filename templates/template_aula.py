# ============================================================
# 📚 Estruturas de Dados — Aula X
# Tema: Pilhas
# Professor: Carlos Roberto
# ============================================================

# 🎯 Objetivo da aula
"""
Ao final desta aula, você será capaz de:
- Entender o conceito de pilha (LIFO)
- Implementar uma pilha em Python
- Aplicar pilhas em problemas reais
"""

# ------------------------------------------------------------
# 📖 1. Contexto'
# ------------------------------------------------------------
"""
Pilhas são estruturas de dados do tipo LIFO (Last In, First Out).

Exemplo real:
- Pilha de pratos
- Botão "voltar" do navegador
"""

# ------------------------------------------------------------
# 🧠 2. Conceito
# ------------------------------------------------------------
"""
Operações principais:
- push() → inserir
- pop() → remover
- peek() → consultar topo
"""

# ------------------------------------------------------------
# 💻 3. Implementação (passo a passo)
# ------------------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


# ------------------------------------------------------------
# 🧪 4. Teste rápido
# ------------------------------------------------------------

s = Stack()
s.push(10)
s.push(20)
print("Topo:", s.peek())
print("Removido:", s.pop())

# ------------------------------------------------------------
# ⚙️ 5. Análise de Complexidade
# ------------------------------------------------------------
"""
push → O(1)
pop → O(1)
peek → O(1)
"""

# ------------------------------------------------------------
# 🚀 6. Exercícios guiados
# ------------------------------------------------------------

# EXERCÍCIO 1:
# Implemente um método size()

# EXERCÍCIO 2:
# Verifique se uma sequência de parênteses é válida

# ------------------------------------------------------------
# 🔥 7. Desafio
# ------------------------------------------------------------
"""
Implemente:
- inversão de string usando pilha
"""

# ------------------------------------------------------------
# 📌 8. Conclusão
# ------------------------------------------------------------
"""
Nesta aula você aprendeu:
- conceito de pilha
- implementação
- aplicações práticas
"""