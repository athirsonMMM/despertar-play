from pathlib import Path
p=Path('_site/story-v0.7.js')
s=p.read_text(encoding='utf-8')
s=s.replace('entregue a prova a Lívia Avelar e fale com o Capitão Caio Ferraz','entregue a prova a Elena Duarte e fale com o Capitão Raul Vilar')
s=s.replace('Todos os capítulos e missões já estão definidos. A implementação jogável será conectada em ordem para não quebrar a base de movimentação e combate.','Todos os capítulos e missões já estão definidos. Os Capítulos 1 e 2 já possuem sequência jogável; os seguintes serão conectados em ordem sem quebrar a base de movimentação e combate.')
p.write_text(s,encoding='utf-8')
