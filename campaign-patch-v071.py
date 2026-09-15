from pathlib import Path
p=Path('_site/index.html')
s=p.read_text(encoding='utf-8')

s=s.replace("[S.CAPTAIN_AFTER]:'Fale com o Capitão após receber a recompensa.'","[S.CAPTAIN_AFTER]:'Fale com Raul Vilar. Ele tem uma nova missão para você.'")
s=s.replace("[S.DONE]:'Tutorial principal concluído.'","[S.DONE]:'Missão principal: Filtros antes de glória. Consulte HISTÓRIA para acompanhar a campanha.'")

old_report="if(mission===S.REPORT){setDialog(base+'<br><br>Você voltou da incursão. Se trouxe a prova da missão, eu posso registrar a conclusão agora.',[['Entregar prova',()=>{player.xp+=100;player.gold+=80;mission=S.CAPTAIN_AFTER;closeDialog();save();updateHud();toastMsg('Missão registrada e recompensa recebida!')}],['Conversar um pouco',()=>helenaVida()],['Depois',closeDialog]]);return}"
new_report="if(mission===S.REPORT){setDialog(base+'<br><br>Você voltou da incursão. Se trouxe a prova da missão, eu posso registrar a conclusão agora.<br><br>Além da recompensa, o Capitão pediu que eu emita uma <b>Carta de Encaminhamento para Orla</b>. É o seu primeiro chamado fora de uma incursão de treinamento.',[['Entregar prova',()=>{player.xp+=100;player.gold+=80;player.guildLetter='Carta de Encaminhamento para Orla';mission=S.CAPTAIN_AFTER;closeDialog();save();updateHud();toastMsg('Carta de Encaminhamento para Orla recebida!')}],['O que é Orla?',()=>setDialog('<b>Helena Duarte</b><br><br>Orla é uma cidade costeira que ainda está reconstruindo bairros próximos das ruínas. A Guilda de lá pediu ajuda porque a Cisterna começou a apresentar anomalias. Raul vai explicar o resto.',['Entregar prova',()=>{player.xp+=100;player.gold+=80;player.guildLetter='Carta de Encaminhamento para Orla';mission=S.CAPTAIN_AFTER;closeDialog();save();updateHud();toastMsg('Carta de Encaminhamento para Orla recebida!')}],['Voltar',()=>talkHelena()])],['Conversar um pouco',()=>helenaVida()],['Depois',closeDialog]]);return}"
if old_report not in s:
    raise SystemExit('report transition not found')
s=s.replace(old_report,new_report,1)

old_after="if(mission===S.CAPTAIN_AFTER){setDialog(base+'<br><br>Você voltou vivo e concluiu a primeira missão. Isso vale mais que qualquer discurso. A partir de agora seu nome começa a existir nos registros da Guilda.',[['E agora?',()=>{mission=S.DONE;closeDialog();save();updateHud();toastMsg('Tutorial concluído!')}],['Conversar mais',()=>raulVida()],['Encerrar',closeDialog]]);return}"
new_after="if(mission===S.CAPTAIN_AFTER){setDialog(base+'<br><br>Você voltou vivo e concluiu a primeira missão. Isso vale mais que qualquer discurso.<br><br>Helena entregou sua carta, certo? Então escute: sua próxima missão se chama <b>Filtros antes de glória</b>. Uma caravana parte para <b>Orla</b>. Você vai levar filtros de água até a Cisterna, ajudar o abrigo e observar uma anomalia que não parece um Portal comum.',[['Explique a missão',()=>setDialog('<b>Raul Vilar</b><br><br>Os relatórios de Orla falam de uma rua que algumas pessoas lembram e outras juram que nunca existiu. A cartógrafa <b>Inês Lume</b> está investigando isso. No abrigo você vai procurar <b>Saira Vento</b>, responsável pelos resgates.<br><br>Seu objetivo inicial é simples: entregar os filtros. Se a situação mudar, siga as orientações de Saira e registre tudo.',['Aceitar: Filtros antes de glória',()=>startEntreVeus()],['Voltar',()=>talkRaul()])],['Aceitar nova missão',()=>startEntreVeus()],['Conversar mais',()=>raulVida()],['Ainda não',closeDialog]]);return}"
if old_after not in s:
    raise SystemExit('captain post-mission transition not found')
s=s.replace(old_after,new_after,1)

insert_after="function raulMissao(){setDialog('<b>Raul Vilar</b><br><br>O portal está estável o bastante para uma incursão curta. Entre, elimine <b>5 Goblins</b> e retorne pelo mesmo ponto. Não persiga nada para além do acampamento.<br><br>Quando voltar, entregue a prova da missão para Helena. Depois venha falar comigo.',[['Entendido. Vou ao quadro.',()=>{mission=S.BOARD;closeDialog();save();updateHud()}],['Voltar',()=>talkRaul()]])}"
helper="""function startEntreVeus(){mission=S.DONE;localStorage.setItem('despertar-campaign-v071',JSON.stringify({chapter:1,mission:'mq_01',completed:[],unlocked:true}));closeDialog();save();updateHud();toastMsg('Nova missão: Filtros antes de glória');window.dispatchEvent(new CustomEvent('despertar:campaign-unlock'))}\n"""
if insert_after not in s:
    raise SystemExit('raulMissao marker not found')
s=s.replace(insert_after,insert_after+'\n'+helper,1)

p.write_text(s,encoding='utf-8')
