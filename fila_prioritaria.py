class FilaPrioritaria:
    codigo:int = 0
    fila:list = []
    clientes_atendidos:list = []
    senha_atual:str = ""

    def gera_senha_atual(self)-> None:
        self.senha_atual = f'PR{self.codigo}'

    def reseta_fila_atual(self)-> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo+=1

    def atualiza_fila(self) -> None:
        self.reseta_fila_atual()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa:int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatistica(self, dia: str, agencia:int, flag:str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia']: int = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.clientes_atendidos
            estatistica['quantidade_clientes_atendidos'] = len(self.clientes_atendidos)

            return estatistica



