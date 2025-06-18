from utils.cores import Cores

class Print:
    @staticmethod
    def cor_token(type):
        if type == 'ID':
            return Cores.OKBLUE
        if type in ('type', 'CONDICIONAL'):
            return Cores.OKCYAN
        if type in ('NINT', 'NREAL'):
            return Cores.OKGREEN
        if type in ('ATRIB', 'OP'):
            return Cores.WARNING
        if type in ('DELIM',):
            return Cores.GRAY
        if type in ('LEITURA', 'ESCRITA'):
            return Cores.HEADER
        if type == 'TOKEN_DESCONHECIDO':
            return Cores.FAIL
        if type == 'EOF':
            return Cores.BOLD
        return Cores.ENDC

    @staticmethod
    def print_banner():
        print(Cores.BOLD + Cores.OKCYAN)
        print("╔════════════════════════════════════════════════════╗")
        print("║           ANÁLISE LÉXICA DE CÓDIGO PASCAL         ║")
        print("╚════════════════════════════════════════════════════╝" + Cores.ENDC)

    @staticmethod
    def print_table(tokens):
        print(Cores.BOLD + "┌─────────────────────┬────────────────────────────┐" + Cores.ENDC)
        print(Cores.BOLD + "│ TOKEN               │ LEXEMA                     │" + Cores.ENDC)
        print(Cores.BOLD + "├─────────────────────┼────────────────────────────┤" + Cores.ENDC)
        for type, lexema in tokens:
            cor = Print.cor_token(type)
            print(f"{cor}│ {type:<19} │ {lexema:<26} │{Cores.ENDC}")
        print(Cores.BOLD + "└─────────────────────┴────────────────────────────┘" + Cores.ENDC)

    @staticmethod
    def print_footer(tokens):
        total = len(tokens) - 1
        print(Cores.OKCYAN + f"\nTotal de tokens reconhecidos: {total}" + Cores.ENDC)
        print(Cores.BOLD + Cores.OKGREEN + "Análise concluída com sucesso! :)\n" + Cores.ENDC)
