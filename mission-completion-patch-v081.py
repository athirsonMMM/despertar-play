from pathlib import Path
import re

p=Path('_site/index.html')
s=p.read_text(encoding='utf-8')

# Patch pequeno: conclusão de missões passa obrigatoriamente pela atendente Elena.
s=s.replace('v0.8.0','v0.8.1')

def sub(pattern,repl,label):
    global s
    s2,n=re.subn(pattern,repl,s,count=1,flags=re.S)
    if n!=1:
        raise SystemExit(f'{label}: replacement count={n}')
    s=s2

# A missão dos 5 Goblins chegava à Guilda ainda em RETURN_GUILD.
# Agora entrar na Guilda após o retorno muda para REPORT, liberando o diálogo de entrega com Elena.
sub(r"function enterGuild\(\)\{.*?\}\nfunction exitGuild",r"""function enterGuild(){world='guild';player.x=540;player.y=610;if(mission===S.GO_GUILD)mission=S.REGISTER;else if(mission===S.RETURN_GUILD)mission=S.REPORT;save();updateHud();toastMsg('Guilda dos Aventureiros')}
function exitGuild""",'guild report transition')

# A recompensa de tutorial precisa passar pelo sistema de XP para permitir level-up corretamente.
if 'player.xp+=100;player.gold+=80;' in s:
    s=s.replace('player.xp+=100;player.gold+=80;','gainXP(100);player.gold+=80;',1)

# Missões procedurais: terminar os alvos não paga no campo.
# O jogador retorna à cidade e entrega o relatório para Elena, que libera XP/Ouro/recursos.
sub(r"function completeDynamicMission\(\)\{.*?\}(?=\nfunction )",r'''function returnDynamicMissionToCity(){ensureMetaSystems();const ai=player.missionAI,a=ai.active;if(!a||!a.ready)return;a.awaitingTurnIn=true;world='city';player.x=1290;player.y=650;projectiles=[];goblins=[];save();updateHud();toastMsg('Objetivo cumprido. Volte à Guilda e entregue o relatório para Elena.')}
function completeDynamicMission(){ensureMetaSystems();const ai=player.missionAI,a=ai.active;if(!a||!a.ready||!a.awaitingTurnIn)return;gainXP(a.rewardXp);player.gold+=a.rewardGold;addResource(a.rewardRes,a.rewardQty);ai.history.unshift({id:a.id,title:a.title,at:Date.now()});ai.history=ai.history.slice(0,20);ai.active=null;ai.offers=[];missionDirectorGenerate(true);closeDialog();save();updateHud();toastMsg(`Missão registrada: +${a.rewardXp} EXP • +${a.rewardGold} Ouro • +${a.rewardQty} ${RESOURCE_LABEL[a.rewardRes]}`)}''','dynamic turn-in functions')

old="if(player.missionAI&&player.missionAI.active&&player.missionAI.active.ready&&near(rift.returnPortal,86)){completeDynamicMission();return}"
new="if(player.missionAI&&player.missionAI.active&&player.missionAI.active.ready&&near(rift.returnPortal,86)){returnDynamicMissionToCity();return}"
if old not in s:
    raise SystemExit('dynamic rift return marker not found')
s=s.replace(old,new,1)

# Elena também finaliza e paga as missões geradas pelo Diretor.
marker="function talkHelena(){\n const intro="
insert="""function talkHelena(){
 ensureMetaSystems();
 const dm=player.missionAI&&player.missionAI.active;
 if(dm&&dm.ready&&dm.awaitingTurnIn){setDialog(`<b>${player.name}</b><br><br>Elena, concluí a missão <b>${dm.title}</b> e vim entregar o relatório.<br><br><b>Elena Duarte</b><br><br>Certo. Vou registrar a conclusão no seu histórico e liberar o pagamento da Guilda.<br><br><b>Recompensa:</b> ${dm.rewardXp} EXP • ${dm.rewardGold} Ouro • ${dm.rewardQty} ${RESOURCE_LABEL[dm.rewardRes]}`,[['Entregar relatório e receber recompensa',()=>completeDynamicMission()],['Depois',closeDialog]]);return}
 const intro="""
if marker not in s:
    raise SystemExit('Elena talk marker not found')
s=s.replace(marker,insert,1)

# Objetivo deixa claro que recompensa só é liberada na Guilda.
old_city="if(world==='city')return`Missão dinâmica: ${a.title}. Vá ao Portal.`"
new_city="if(world==='city')return a.ready&&a.awaitingTurnIn?'Missão concluída. Retorne à Guilda e fale com Elena.':`Missão dinâmica: ${a.title}. Vá ao Portal.`;if(world==='guild'&&a.ready&&a.awaitingTurnIn)return'Fale com Elena para registrar a missão e receber a recompensa.'"
if old_city not in s:
    raise SystemExit('dynamic objective marker not found')
s=s.replace(old_city,new_city,1)

# A seta também leva à Guilda/Elena durante uma entrega pendente.
old_target="function target(){"
new_target="function target(){if(player.missionAI&&player.missionAI.active&&player.missionAI.active.ready&&player.missionAI.active.awaitingTurnIn){if(world==='city')return city.guildDoor;if(world==='guild')return guild.reception}"
if old_target not in s:
    raise SystemExit('target marker not found')
s=s.replace(old_target,new_target,1)

# Quadro informa que a missão está aguardando entrega, em vez de mandar o jogador de volta ao portal.
old_board="if(ai.active){const a=ai.active;setDialog(`<b>Diretor de Missões — missão ativa</b><br><br><b>${a.title}</b> • Rank ${a.rank}<br>${a.place}<br>Progresso: ${a.kills||0}/${a.target}<br>Recompensa: ${a.rewardXp} EXP • ${a.rewardGold} Ouro • ${a.rewardQty} ${RESOURCE_LABEL[a.rewardRes]}`,[['Ir ao Portal',()=>{closeDialog();if(world==='guild'){exitGuild();toastMsg('Siga até o Portal da cidade.')}}],['Abandonar missão',()=>{ai.active=null;save();showDynamicBoard()}],['Fechar',closeDialog]]);return}"
new_board="if(ai.active){const a=ai.active;if(a.ready&&a.awaitingTurnIn){setDialog(`<b>Diretor de Missões — objetivo cumprido</b><br><br><b>${a.title}</b><br>Retorne à atendente <b>Elena Duarte</b> para registrar a conclusão e receber:<br>${a.rewardXp} EXP • ${a.rewardGold} Ouro • ${a.rewardQty} ${RESOURCE_LABEL[a.rewardRes]}`,[['Fechar',closeDialog]]);return}setDialog(`<b>Diretor de Missões — missão ativa</b><br><br><b>${a.title}</b> • Rank ${a.rank}<br>${a.place}<br>Progresso: ${a.kills||0}/${a.target}<br>Recompensa: ${a.rewardXp} EXP • ${a.rewardGold} Ouro • ${a.rewardQty} ${RESOURCE_LABEL[a.rewardRes]}`,[['Ir ao Portal',()=>{closeDialog();if(world==='guild'){exitGuild();toastMsg('Siga até o Portal da cidade.')}}],['Abandonar missão',()=>{ai.active=null;save();showDynamicBoard()}],['Fechar',closeDialog]]);return}"
if old_board not in s:
    raise SystemExit('dynamic board marker not found')
s=s.replace(old_board,new_board,1)

for needle in ["else if(mission===S.RETURN_GUILD)mission=S.REPORT","Entregar relatório e receber recompensa","returnDynamicMissionToCity","v0.8.1"]:
    if needle not in s:
        raise SystemExit(f'validation failed: {needle}')

p.write_text(s,encoding='utf-8')
