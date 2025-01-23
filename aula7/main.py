import time


def simular_api_paginada(pagina_atual):
    """
    Simula o consumo de uma API paginada.
    Retorna um dicionário com os dados da página atual e a informação sobre a próxima página.
    """
    # Dados simulados (como se fossem retornados pela API)
    dados_por_pagina = {
        1: {"dados": ["item1", "item2", "item3"], "proxima_pagina": 2},
        2: {"dados": ["item4", "item5"], "proxima_pagina": 3},
        3: {"dados": ["item6", "item7", "item8", "item9"], "proxima_pagina": None},
    }

    # Simula a resposta da API (com um pequeno atraso para parecer mais real)
    time.sleep(1)
    return dados_por_pagina.get(pagina_atual, {"dados": [], "proxima_pagina": None})
