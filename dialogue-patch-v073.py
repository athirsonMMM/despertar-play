from pathlib import Path

p=Path('_site/index.html')
s=p.read_text(encoding='utf-8')

# Patch visual version only; keep save keys/progress compatible.
s=s.replace('v0.7.2','v0.7.3')

# Keep function names stable internally, but show the NPC name as Elena consistently.
s=s.replace('Helena Duarte','Elena Duarte')
s=s.replace('Fale com Helena','Fale com Elena')
s=s.replace('Helena já','Elena já')
s=s.replace('Helena entregou','Elena entregou')
s=s.replace('entregue a prova da missão para Helena','entregue a prova da missão para Elena')
s=s.replace('Se Helena mandar','Se Elena mandar')

def between(start,end,new,label):
    global s
    a=s.find(start)
    if a<0: raise SystemExit(f'{label}: start not found')
    b=s.find(end,a)
    if b<0: raise SystemExit(f'{label}: end not found')
    s=s[:a]+new+'\n'+s[b:]

between('function talkHelena(){','function helenaVida(){',r'''function talkHelena(){
 const intro=`<b>${player.name}</b><br><br>Olá. Quero me registrar como <b>Desperto</b> e começar a trabalhar com missões da Guilda.<br><br><b>Elena Duarte — Atendente da Guilda</b><br><br>Olá. Eu sou <b>Elena</b>. Trabalho aqui na Guilda desde os primeiros meses depois da Catástrofe. Sou responsável pelo registro dos Despertos, pelas carteirinhas e pela documentação das missões.`;
 if(mission===S.REPORT){setDialog(`<b>${player.name}</b><br><br>Elena, voltei da missão dos Goblins. Vim entregar a prova da conclusão.<br><br><b>Elena Duarte</b><br><br>Certo. Vou conferir e registrar sua primeira missão oficial. O Capitão também pediu que eu prepare uma <b>Carta de Encaminhamento para Orla</b> para você.`,[['Entregar prova',()=>{player.xp+=100;player.gold+=80;player.guildLetter='Carta de Encaminhamento para Orla';mission=S.CAPTAIN_AFTER;closeDialog();save();updateHud();toastMsg('Carta de Encaminhamento para Orla recebida!')}],['Quem é você?',()=>helenaVida()],['Sobre a Guilda',()=>helenaGuilda()],['Depois',closeDialog]]);return}
 if(mission===S.REGISTER){setDialog(intro,[['Quero me registrar',()=>helenaRegistro()],['Quem é você?',()=>helenaVida()],['Como surgiu a Guilda?',()=>helenaGuilda()],['Agora não',closeDialog]]);return}
 setDialog(`<b>${player.name}</b><br><br>Olá, Elena.<br><br><b>Elena Duarte</b><br><br>Olá, ${player.name}. Em que posso ajudar?`,[['Quem é você?',()=>helenaVida()],['Sobre a Guilda',()=>helenaGuilda()],['Encerrar',closeDialog]])
}''','Elena talk')

between('function helenaVida(){','function helenaGuilda(){',r'''function helenaVida(){setDialog('<b>Elena Duarte</b><br><br>Antes da Catástrofe eu trabalhava com registros e organização de documentos. Quando tudo começou, passei a ajudar sobreviventes com listas de pessoas, suprimentos e identificação. Depois vim trabalhar na Guilda e continuei nessa função.<br><br>Não tem muito mistério. Eu prefiro manter as coisas organizadas porque, depois do que aconteceu, um nome perdido em um papel pode significar uma pessoa esquecida.',[['Como surgiu a Guilda?',()=>helenaGuilda()],['Voltar',()=>talkHelena()],['Encerrar',closeDialog]])}''','Elena bio')

between('function helenaGuilda(){','function helenaRegistro(){',r'''function helenaGuilda(){setDialog('<b>Elena Duarte</b><br><br>A Guilda surgiu depois das primeiras ondas de Portais. Os Despertos estavam entrando sem organização, sem registro e muitas equipes simplesmente não voltavam.<br><br>Então começaram a reunir informações, classificar riscos, registrar missões e criar os Ranks. Hoje a Guilda serve para organizar os Despertos, proteger as cidades e evitar que alguém aceite uma missão muito acima da própria capacidade.',mission===S.REGISTER?[['Quero me registrar',()=>helenaRegistro()],['Voltar',()=>talkHelena()],['Pular explicação',()=>helenaRegistro()]]:[['Voltar',()=>talkHelena()],['Encerrar',closeDialog]])}''','Guild lore')

between('function helenaRegistro(){','function talkRaul(){',r'''function helenaRegistro(){setDialog(`<b>${player.name}</b><br><br>Quero fazer meu registro.<br><br><b>Elena Duarte</b><br><br>Certo. Vou registrar seu nome, sua classe e seu Despertar. Como você está começando agora, sua identificação será <b>Rank F</b>. Depois disso, fale com o Capitão Raul para receber sua primeira orientação de missão.`,[['Concluir registro',()=>{player.guildRegistered=true;player.guildCard=true;mission=S.CAPTAIN;closeDialog();save();updateHud();toastMsg('Carteirinha Rank F recebida!')}],['Voltar',()=>talkHelena()]])}''','Elena register')

between('function talkRaul(){','function raulVida(){',r'''function talkRaul(){
 const intro=`<b>${player.name}</b><br><br>Olá. Sou ${player.name}. Acabei de me registrar como Desperto e quero começar a fazer missões.<br><br><b>Raul Vilar — Capitão de Incursões</b><br><br>Raul Vilar. Eu coordeno as missões e as equipes de incursão desta Guilda. Se você acabou de receber o Rank F, vamos começar pelo básico e ver como você se sai.`;
 if(mission===S.CAPTAIN){setDialog(intro,[['Quero começar',()=>raulMissao()],['Quem é você?',()=>raulVida()],['Como funcionam as missões?',()=>raulSistemaMissoes()],['Agora não',closeDialog]]);return}
 if(mission===S.CAPTAIN_AFTER){setDialog(`<b>${player.name}</b><br><br>Capitão, concluí a missão dos Goblins e já entreguei a prova para Elena.<br><br><b>Raul Vilar</b><br><br>Bom. Sua primeira missão foi registrada. Elena deve ter entregue sua carta de encaminhamento. A partir de agora você entra numa missão de verdade: <b>Filtros antes de glória</b>. Uma caravana vai para Orla e precisamos de um Desperto acompanhando os suprimentos.`,[['Explique a missão',()=>setDialog('<b>Raul Vilar</b><br><br>Os relatórios de Orla falam de uma rua que algumas pessoas lembram e outras juram que nunca existiu. A cartógrafa <b>Inês Lume</b> está investigando isso. No abrigo você vai procurar <b>Saira Vento</b>, responsável pelos resgates.<br><br>Seu primeiro objetivo é entregar os filtros. Se a situação mudar, siga as orientações de Saira e registre tudo.',[['Aceitar: Filtros antes de glória',()=>startEntreVeus()],['Voltar',()=>talkRaul()]])],['Aceitar nova missão',()=>startEntreVeus()],['Quem é você?',()=>raulVida()],['Ainda não',closeDialog]]);return}
 setDialog(`<b>${player.name}</b><br><br>Olá, Capitão.<br><br><b>Raul Vilar</b><br><br>Fale. Se for sobre missão, diga o que precisa.`,[['Quem é você?',()=>raulVida()],['Como funcionam as missões?',()=>raulSistemaMissoes()],['Sobre a cidade',()=>raulCidade()],['Encerrar',closeDialog]])
}''','Raul talk')

between('function raulVida(){','function raulCidade(){',r'''function raulVida(){setDialog('<b>Raul Vilar</b><br><br>Antes da Catástrofe eu trabalhava com segurança e operações de campo. Depois das primeiras invasões, comecei a organizar grupos de sobreviventes e, mais tarde, equipes de Despertos.<br><br>Hoje fico responsável por avaliar missões e evitar que gente inexperiente entre em um Portal sem saber no que está se metendo.',[['Como funcionam as missões?',()=>raulSistemaMissoes()],['Voltar',()=>talkRaul()],['Encerrar',closeDialog]])}
function raulSistemaMissoes(){setDialog('<b>Raul Vilar</b><br><br>A Guilda recebe pedidos da cidade, relatórios de Portais e chamados de outras regiões. Cada missão recebe um Rank de risco. Você começa no Rank F e vai construindo histórico.<br><br>Complete missões, entregue as provas e seu registro vai abrir trabalhos mais difíceis. O Quadro mostra o que está disponível para você.',mission===S.CAPTAIN?[['Quero começar',()=>raulMissao()],['Voltar',()=>talkRaul()]]:[['Voltar',()=>talkRaul()],['Encerrar',closeDialog]])}''','Raul bio/system')

# Make direct clicks on nearby named NPCs open conversation while preserving attack elsewhere.
old="c.addEventListener('mousedown',e=>{if(e.button!==0||!player||dialog.style.display==='block')return;basicAttack(mouse.x+cam.x-player.x,mouse.y+cam.y-player.y)});"
new="""c.addEventListener('mousedown',e=>{if(e.button!==0||!player||dialog.style.display==='block')return;const r=c.getBoundingClientRect(),sx=(e.clientX-r.left)*W/r.width,sy=(e.clientY-r.top)*H/r.height,wx=sx+cam.x,wy=sy+cam.y;const clicked=(o,rad=30)=>Math.hypot(wx-o.x,wy-o.y)<rad;if(world==='guild'&&near(guild.reception,90)&&clicked(guild.reception,34)){talkHelena();return}if(world==='guild'&&near(guild.captain,90)&&clicked(guild.captain,36)){talkRaul();return}if(world==='guild'&&near({x:520,y:290},90)&&clicked({x:520,y:290},34)){talkCaio();return}if(world==='guild'&&near({x:570,y:360},90)&&clicked({x:570,y:360},34)){talkMirela();return}if(world==='city'&&near({x:470,y:500},90)&&clicked({x:470,y:500},34)){talkDavi();return}if(world==='city'&&near({x:1080,y:480},90)&&clicked({x:1080,y:480},34)){talkBreno();return}basicAttack(wx-player.x,wy-player.y)});"""
if old not in s: raise SystemExit('mouse interaction handler not found')
s=s.replace(old,new,1)

p.write_text(s,encoding='utf-8')
