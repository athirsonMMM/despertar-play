from pathlib import Path
import re

p=Path('_site/index.html')
s=p.read_text(encoding='utf-8')

def rep(old,new,label):
    global s
    if old not in s:
        raise SystemExit(f'{label} not found')
    s=s.replace(old,new,1)

def sub(pattern,repl,label):
    global s
    s2,n=re.subn(pattern,repl,s,count=1,flags=re.S)
    if n!=1:
        raise SystemExit(f'{label} replacement count={n}')
    s=s2

# Patch version only; keep v0.7.1 save keys so existing testers do not lose progress.
s=s.replace('v0.7.1','v0.7.2')

# Natural NPC introductions: personal history stays behind optional conversation choices.
rep(
"const base=`<b>Helena Duarte — Atendente da Guilda</b><br><br>Oi. Meu nome é <b>Helena Duarte</b>. Trabalho neste balcão desde que a Guilda reabriu as portas depois da Queda. Moro no setor leste da cidade com minha mãe e meu irmão mais novo.<br><br>Eu cuido dos registros, carteirinhas, recompensas e relatórios de missão.`;",
"const base=`<b>Helena Duarte — Atendente da Guilda</b><br><br>Oi. Meu nome é <b>Helena Duarte</b>. Trabalho na Guilda desde que ela reabriu depois da Queda.<br><br>Eu faço registros de novos Despertos, emito carteirinhas, registro conclusões de missão e organizo as recompensas.`;",
'helena intro')
rep(
"function helenaVida(){setDialog('<b>Helena Duarte</b><br><br>Antes da invasão eu estudava administração. Depois que os portais apareceram, papéis viraram fichas de racionamento, listas de desaparecidos e registros de Despertos. Acabei ficando boa nisso.<br><br>Meu pai desapareceu durante a evacuação da zona sul. Desde então, minha família ficou aqui. Não é uma vida tranquila, mas esta cidade virou nossa casa.',[['E a Guilda?',()=>helenaGuilda()],['Voltar',()=>talkHelena()],['Encerrar',closeDialog]])}",
"function helenaVida(){setDialog('<b>Helena Duarte</b><br><br>Antes da invasão eu estudava administração. Vim para esta cidade durante as primeiras evacuações e comecei ajudando a organizar fichas de racionamento e listas de desaparecidos. Quando a Guilda foi criada, passei a trabalhar aqui.<br><br>Parte da minha família sobreviveu comigo. Foi por isso que eu preferi continuar neste trabalho: um registro certo pode ser a diferença entre alguém ser encontrado ou simplesmente desaparecer dos papéis.',[['E a Guilda?',()=>helenaGuilda()],['Voltar',()=>talkHelena()],['Encerrar',closeDialog]])}",
'helena bio')
rep(
"const base='<b>Raul Vilar — Capitão de Incursões</b><br><br>Raul Vilar. Capitão de incursões desta filial. Antes da Queda eu era sargento do Exército; hoje meu trabalho é decidir quem entra num portal e aumentar a chance de essa pessoa voltar.';",
"const base='<b>Raul Vilar — Capitão de Incursões</b><br><br>Meu nome é <b>Raul Vilar</b>. Sou o capitão responsável pelas incursões desta Guilda. Eu organizo equipes, avalio riscos e acompanho as missões que saem da cidade.';",
'raul intro')
rep(
"function raulVida(){setDialog('<b>Raul Vilar</b><br><br>Eu cheguei aqui com uma coluna de sobreviventes três meses depois da primeira onda. Minha esposa não chegou. Desde então fiquei responsável pelos grupos de incursão. Não gosto de mandar gente para lugares onde eu mesmo não pisaria.<br><br>Se eu disser para recuar, recue. Orgulho mata mais aventureiros do que monstros.',[['Sobre a cidade',()=>raulCidade()],['Voltar',()=>talkRaul()],['Encerrar',closeDialog]])}",
"function raulVida(){setDialog('<b>Raul Vilar</b><br><br>Antes da Queda eu era sargento do Exército. Cheguei aqui com uma coluna de sobreviventes alguns meses depois da primeira onda e acabei assumindo a organização das primeiras equipes que entravam nos Portais.<br><br>Perdi gente demais em incursões mal planejadas. Por isso eu não mando um Desperto para um lugar onde eu mesmo não pisaria. Se eu disser para recuar, recue.',[['Sobre a cidade',()=>raulCidade()],['Voltar',()=>talkRaul()],['Encerrar',closeDialog]])}",
'raul bio')

# Orla and Cisterna playable maps.
camp_line="const camp={w:1300,h:760,returnPortal:{x:110,y:640,r:36},obstacles:[{x:420,y:130,w:85,h:90},{x:700,y:140,w:85,h:90},{x:870,y:420,w:90,h:95},{x:555,y:360,w:80,h:42}]};"
extra_maps="""const orlaDeparture={x:220,y:760,r:38};
const orla={w:1600,h:900,returnGate:{x:105,y:780,r:38},saira:{x:330,y:235,r:22},ines:{x:975,y:230,r:22},cisternDoor:{x:1370,y:655,r:42},residents:[{id:'morador_a',name:'Morador preso',x:590,y:575},{id:'morador_b',name:'Moradora presa',x:820,y:650},{id:'morador_c',name:'Idoso preso',x:1040,y:555}],clues:[{id:'placa',name:'Placa molhada',x:725,y:330},{id:'mapa',name:'Marco cartográfico',x:1080,y:355},{id:'casa',name:'Casa sem registro',x:1240,y:440}],obstacles:[]};
const cistern={w:1200,h:760,exit:{x:90,y:650,r:38},returnPortal:{x:1090,y:650,r:40},valves:[{id:'v1',x:360,y:210},{id:'v2',x:650,y:390},{id:'v3',x:900,y:225}],obstacles:[]};
function mapForWorld(){return world==='city'?city:world==='guild'?guild:world==='orla'?orla:world==='cistern'?cistern:camp}"
rep(camp_line,camp_line+'\n'+extra_maps,'map insertion')

# Campaign state, inventory, leveling and the complete playable Chapter 1 loop.
old_start="function startEntreVeus(){mission=S.DONE;localStorage.setItem('despertar-campaign-v071',JSON.stringify({chapter:1,mission:'mq_01',completed:[],unlocked:true}));closeDialog();save();updateHud();toastMsg('Nova missão: Filtros antes de glória');window.dispatchEvent(new CustomEvent('despertar:campaign-unlock'))}"
new_start=r'''const CAMPAIGN_MAIN='despertar-campaign-v071';
function readCampaignMain(){try{return JSON.parse(localStorage.getItem(CAMPAIGN_MAIN)||'null')}catch{return null}}
function writeCampaignMain(st){localStorage.setItem(CAMPAIGN_MAIN,JSON.stringify(st))}
function ensureCampaignMain(){let st=readCampaignMain();if(!st)st={chapter:1,mission:'mq_01',completed:[],unlocked:true};if(!Array.isArray(st.completed))st.completed=[];if(!st.progress)st.progress={};return st}
function currentCampaignMission(){const st=readCampaignMain();return st&&st.unlocked?st.mission:null}
function progressMain(){const st=ensureCampaignMain();return st.progress||{}}
function saveProgressMain(pr){const st=ensureCampaignMain();st.progress=pr;writeCampaignMain(st)}
function ensureInventory(){if(!player.inventory||typeof player.inventory!=='object')player.inventory={};return player.inventory}
function addItem(name,qty=1){const inv=ensureInventory();inv[name]=(inv[name]||0)+qty}
function removeItem(name,qty=1){const inv=ensureInventory();if((inv[name]||0)<qty)return false;inv[name]-=qty;if(inv[name]<=0)delete inv[name];return true}
function gainXP(amount){player.xp=Number(player.xp||0)+amount;let leveled=false;while(true){const need=100+Math.max(0,(player.level||1)-1)*50;if(player.xp<need)break;player.xp-=need;player.level=(player.level||1)+1;player.maxHp+=8;player.hp=player.maxHp;leveled=true}if(leveled)toastMsg(`Nível ${player.level} alcançado!`)}
function campaignReward(id,next,xp,gold,drop){const st=ensureCampaignMain();if(st.completed.includes(id))return;gainXP(xp);player.gold=Number(player.gold||0)+gold;if(drop)addItem(drop,1);st.completed.push(id);st.mission=next;st.chapter=next==='mq_05'?2:1;st.progress={};writeCampaignMain(st);save();updateHud();const item=drop?` • Drop: ${drop}`:'';toastMsg(`Missão concluída: +${xp} EXP • +${gold} Ouro${item}`);window.dispatchEvent(new CustomEvent('despertar:campaign-progress'))}
function campaignObjective(){const st=readCampaignMain();if(!st||!st.unlocked)return'Fale com Raul Vilar para receber a próxima missão.';const pr=st.progress||{};if(st.mission==='mq_01')return world==='orla'?'Entregue a caixa de filtros para Saira Vento.':'Vá até a caravana marcada e viaje para Orla.';if(st.mission==='mq_02')return`Resgate os moradores da área alagada (${(pr.rescued||[]).length}/3).`;if(st.mission==='mq_03')return (pr.clues||[]).length<3?`Investigue as inconsistências da rua (${(pr.clues||[]).length}/3).`:'Fale com Inês Lume e compare as três evidências.';if(st.mission==='mq_04'){if(world!=='cistern')return'Entre na Cisterna e investigue o padrão.';if((pr.valves||[]).length<3)return`Interrompa as válvulas do padrão (${(pr.valves||[]).length}/3).`;return pr.bossDefeated?'Use o portal de retorno.':'Derrote o Síndico da Cisterna.'}if(st.mission==='mq_05')return'Capítulo 1 concluído. Nova missão liberada: Carta sem destinatário.';return'Continue a campanha principal.'}
function startEntreVeus(){mission=S.DONE;const old=readCampaignMain();const st=old&&old.unlocked?old:{chapter:1,mission:'mq_01',completed:[],unlocked:true,progress:{}};st.unlocked=true;st.chapter=1;st.mission='mq_01';st.progress=st.progress||{};writeCampaignMain(st);addItem('Caixa de Filtros',1);closeDialog();save();updateHud();toastMsg('Nova missão: Filtros antes de glória');window.dispatchEvent(new CustomEvent('despertar:campaign-unlock'))}
function travelOrla(){world='orla';player.x=180;player.y=735;projectiles=[];goblins=[];save();updateHud();toastMsg('Orla — Distrito da Cisterna')}
function travelCityFromOrla(){world='city';player.x=260;player.y=735;projectiles=[];goblins=[];save();updateHud();toastMsg('Cidade Inicial')}
function spawnCisternBoss(){const st=ensureCampaignMain(),pr=st.progress||{};if(st.mission==='mq_04'&&(pr.valves||[]).length>=3&&!pr.bossDefeated){const hp=Math.max(1,Number(pr.bossHp||180));goblins=[{x:820,y:520,r:28,hp,maxHp:180,dead:false,id:99,state:'idle',cooldown:.8,windup:0,attackX:0,attackY:0,boss:true}]}else goblins=[]}
function enterCistern(){world='cistern';player.x=130;player.y=630;projectiles=[];spawnCisternBoss();save();updateHud();toastMsg('Cisterna de Orla')}
function exitCistern(){world='orla';player.x=1290;player.y=650;projectiles=[];goblins=[];save();updateHud();toastMsg('Retorno a Orla')}
function talkSaira(){const cm=currentCampaignMission();if(cm==='mq_01'){setDialog('<b>Saira Vento — Capitã de Resgate</b><br><br>Você é o Desperto que Raul enviou? Ótimo. Os filtros chegaram na hora certa. A água da cisterna ficou turva desde que a rua começou a... mudar.<br><br>Entregue a caixa e eu coloco uma equipe para distribuir tudo.',[['Entregar filtros',()=>{if(!removeItem('Caixa de Filtros',1))addItem('Caixa de Filtros',1),removeItem('Caixa de Filtros',1);closeDialog();campaignReward('mq_01','mq_02',40,25);toastMsg('Nova missão: Quem ficou na água')}],['Quem é você?',()=>setDialog('<b>Saira Vento</b><br><br>Eu coordeno resgates em Orla. Quando uma área desaba, alaga ou muda de lugar por causa das Dobras, minha equipe entra para tirar as pessoas antes de tentar entender o fenômeno.',[['Voltar',()=>talkSaira()],['Encerrar',closeDialog]])],['Depois',closeDialog]]);return}if(cm==='mq_02'){setDialog('<b>Saira Vento</b><br><br>Três moradores ficaram presos na faixa alagada. Vá até cada um e use os pontos de ancoragem. Não tente atravessar a parte mais funda.',[['Entendido',closeDialog]]) ;return}setDialog('<b>Saira Vento</b><br><br>Continue atento. Em Orla, quando uma coisa parece errada, normalmente existem duas coisas erradas por trás dela.')}
function rescueResident(id,name){const st=ensureCampaignMain(),pr=st.progress||{};pr.rescued=pr.rescued||[];if(pr.rescued.includes(id)){toastMsg('Este morador já foi resgatado.');return}setDialog(`<b>${name}</b><br><br>A água está subindo. Há uma corda de ancoragem presa à estrutura ao lado.`,[['Puxar para a área segura',()=>{pr.rescued.push(id);st.progress=pr;writeCampaignMain(st);closeDialog();save();if(pr.rescued.length>=3){campaignReward('mq_02','mq_03',70,40);toastMsg('Nova missão: Uma placa, duas ruas')}else{updateHud();toastMsg(`Resgate ${pr.rescued.length}/3`)}}],['Depois',closeDialog]])}
function inspectClue(id,title,text){const st=ensureCampaignMain(),pr=st.progress||{};pr.clues=pr.clues||[];if(pr.clues.includes(id)){setDialog(`<b>${title}</b><br><br>Você já registrou esta evidência.`);return}setDialog(`<b>${title}</b><br><br>${text}`,[['Registrar evidência',()=>{pr.clues.push(id);st.progress=pr;writeCampaignMain(st);closeDialog();save();updateHud();toastMsg(`Evidência ${(pr.clues||[]).length}/3 registrada`)}],['Depois',closeDialog]])}
function talkInes(){const cm=currentCampaignMission(),pr=progressMain();if(cm==='mq_03'&&(pr.clues||[]).length>=3){setDialog('<b>Inês Lume — Cartógrafa</b><br><br>As três evidências entram em conflito, mas nenhuma parece falsa. A placa aponta uma rua. O marco cartográfico nega que ela exista. E a casa carrega marcas de uso onde o mapa mostra um terreno vazio.<br><br>Não escolha uma versão ainda. A origem da diferença está na cisterna.',[['Concluir investigação',()=>{closeDialog();campaignReward('mq_03','mq_04',90,55);toastMsg('Nova missão: O fundo responde')}],['Quem é você?',()=>setDialog('<b>Inês Lume</b><br><br>Sou cartógrafa. Desde que as Dobras começaram, mapas deixaram de ser apenas desenhos de lugares. Às vezes eles são provas de que alguma coisa foi apagada.',[['Voltar',()=>talkInes()],['Encerrar',closeDialog]])],['Depois',closeDialog]]);return}setDialog('<b>Inês Lume</b><br><br>Não tente decidir qual lembrança é a verdadeira antes de reunir as evidências. Em fenômenos assim, uma resposta rápida costuma apagar metade do problema.')}
function activateValve(id){const st=ensureCampaignMain(),pr=st.progress||{};pr.valves=pr.valves||[];if(pr.valves.includes(id)){toastMsg('Válvula já interrompida.');return}pr.valves.push(id);st.progress=pr;writeCampaignMain(st);save();if(pr.valves.length>=3){pr.bossHp=180;st.progress=pr;writeCampaignMain(st);spawnCisternBoss();toastMsg('O padrão rompeu — Síndico da Cisterna despertou!')}else toastMsg(`Válvula interrompida ${pr.valves.length}/3`)}'''
rep(old_start,new_start,'campaign helpers')

# Goblin mission payment now goes through the XP system and visibly confirms payment.
s=s.replace('player.xp+=100;player.gold+=80;','gainXP(100);player.gold+=80;')
s=s.replace("toastMsg('Carta de Encaminhamento para Orla recebida!')","toastMsg('Pagamento: +100 EXP • +80 Ouro • Carta para Orla recebida!')")

# Dynamic campaign objective after tutorial.
s=s.replace("[S.DONE]:'Missão principal: Filtros antes de glória. Consulte HISTÓRIA para acompanhar a campanha.'","[S.DONE]:campaignObjective()")

# Existing saves can enter the new maps.
sub(r"function load\(\)\{.*?\}\nfunction showGame",r"""function load(){try{const s=JSON.parse(localStorage.getItem(SAVE));if(!s)return false;player=s.player;ensureInventory();world=s.world||'city';mission=s.mission||S.GO_GUILD;if(world==='camp'){spawnGoblins();(s.goblins||[]).forEach((v,i)=>Object.assign(goblins[i],v))}else if(world==='cistern'){spawnCisternBoss()}showGame();return true}catch{return false}}
function showGame""",'load function')

# Visible XP in HUD for reward testing.
s=s.replace("document.getElementById('who').textContent=`${player.name} • ${player.class} • Nv.${player.level} • Rank ${player.rank}`;","document.getElementById('who').textContent=`${player.name} • ${player.class} • Nv.${player.level} • EXP ${player.xp||0} • Rank ${player.rank}`;")

# Combat works in the Chapter 1 boss room too.
s=s.replace("if(world!=='camp'){updateHud();return}","if(world!=='camp'&&world!=='cistern'){updateHud();return}",1)
s=s.replace("if(world==='camp'){for(const p of projectiles)","if(world==='camp'||world==='cistern'){for(const p of projectiles)",1)
s=s.replace("if(!(camp.obstacles||[]).some(o=>circleRectHit(nx,ny,g.r,o)))","if(!((world==='cistern'?cistern:camp).obstacles||[]).some(o=>circleRectHit(nx,ny,g.r,o)))",1)

# Drops, XP and gold on combat kills; boss reward closes MQ04.
sub(r"function hitGoblin\(g,d\)\{.*?\}\nfunction basicAttack",r'''function hitGoblin(g,d){if(g.dead)return;g.hp-=d;if(g.hp<=0){g.hp=0;g.dead=true;g.state='dead';if(world==='camp'){gainXP(8);player.gold=Number(player.gold||0)+5;addItem('Fragmento de Goblin',1);toastMsg('Drop: +8 EXP • +5 Ouro • Fragmento de Goblin');save()}else if(world==='cistern'&&g.boss){const st=ensureCampaignMain(),pr=st.progress||{};pr.bossDefeated=true;pr.bossHp=0;st.progress=pr;writeCampaignMain(st);campaignReward('mq_04','mq_05',180,120,'Inscrição de Namar');toastMsg('BOSS derrotado • Drop: Inscrição de Namar • Capítulo 1 concluído')}}else if(world==='cistern'&&g.boss){const st=ensureCampaignMain(),pr=st.progress||{};pr.bossHp=g.hp;st.progress=pr;writeCampaignMain(st)}updateHud()}
function basicAttack''','hitGoblin')

# Movement stays unchanged except selecting the correct map boundaries.
sub(r"function tryMove\(nx,ny\)\{.*?\}\nfunction hurtPlayer",r"""function tryMove(nx,ny){const map=mapForWorld();player.x=Math.max(28,Math.min(map.w-28,nx));player.y=Math.max(28,Math.min(map.h-28,ny))}
function hurtPlayer""",'tryMove')

# City caravan interaction and playable Orla/Cisterna interactions.
city_portal="if(near(city.portal,86)&&mission===S.PORTAL){setDialog('<b>Portal Rank F</b><br>Missão ativa: Infestação de Goblins',[['Entrar',()=>{closeDialog();enterCamp()}],['Cancelar',closeDialog]]);return}"
rep(city_portal,city_portal+"\n  const campaignNow=readCampaignMain();if(campaignNow&&campaignNow.unlocked&&near(orlaDeparture,86)){travelOrla();return}",'city caravan interaction')

camp_return=" if(world==='camp'&&goblins.filter(g=>g.dead).length>=5&&near(camp.returnPortal,86)){setDialog('<b>Portal de retorno</b><br>A missão foi concluída. Volte à Guilda para entregar a prova.',[['Retornar à cidade',()=>{closeDialog();returnCity()}],['Ficar',closeDialog]])}"
extra_interact=r''' if(world==='orla'){
  const cm=currentCampaignMission(),pr=progressMain();
  if(near(orla.returnGate,82)){travelCityFromOrla();return}
  if(near(orla.saira,74)){talkSaira();return}
  if(near(orla.ines,74)){talkInes();return}
  if(cm==='mq_02'){for(const r of orla.residents)if(!(pr.rescued||[]).includes(r.id)&&near(r,68)){rescueResident(r.id,r.name);return}}
  if(cm==='mq_03'){for(const q of orla.clues)if(!(pr.clues||[]).includes(q.id)&&near(q,68)){const texts={placa:'A placa mostra um nome de rua que não aparece no mapa atual. A tinta está desgastada, mas os parafusos são recentes.',mapa:'O marco de coordenadas confirma o traçado oficial. Segundo ele, a rua termina antes da casa que alguns moradores lembram.',casa:'As paredes exibem marcas de móveis e reparos antigos, embora os registros indiquem que este lote sempre esteve vazio.'};inspectClue(q.id,q.name,texts[q.id]);return}}
  if(cm==='mq_04'&&near(orla.cisternDoor,90)){setDialog('<b>Entrada da Cisterna</b><br><br>O ruído das válvulas forma um padrão que se repete de maneira impossível. Inês acredita que a origem da anomalia está lá embaixo.',[['Entrar',()=>{closeDialog();enterCistern()}],['Depois',closeDialog]]);return}
 }
 if(world==='cistern'){
  const cm=currentCampaignMission(),pr=progressMain();
  if(near(cistern.exit,82)&&cm==='mq_04'){exitCistern();return}
  if(cm==='mq_04'){for(const v of cistern.valves)if(!(pr.valves||[]).includes(v.id)&&near(v,70)){activateValve(v.id);return}}
  if(cm==='mq_05'&&near(cistern.returnPortal,88)){exitCistern();return}
 }
'''
rep(camp_return,extra_interact+camp_return,'orla interactions')

# Target arrows for the four missions.
sub(r"function target\(\)\{.*?\}\nfunction arrowToTarget",r'''function target(){if(world==='camp'&&mission===S.GOBLINS){const alive=goblins.find(g=>!g.dead);return alive||camp.returnPortal}if(world==='city'){if(mission===S.GO_GUILD||mission===S.RETURN_GUILD)return city.guildDoor;if(mission===S.PORTAL)return city.portal;if(mission===S.DONE&&currentCampaignMission())return orlaDeparture}if(world==='guild'){if(mission===S.REGISTER||mission===S.REPORT)return guild.reception;if(mission===S.CAPTAIN||mission===S.CAPTAIN_AFTER)return guild.captain;if(mission===S.BOARD)return guild.board;if(mission===S.PORTAL)return guild.exit}if(world==='orla'){const cm=currentCampaignMission(),pr=progressMain();if(cm==='mq_01')return orla.saira;if(cm==='mq_02')return orla.residents.find(r=>!(pr.rescued||[]).includes(r.id))||orla.saira;if(cm==='mq_03')return orla.clues.find(q=>!(pr.clues||[]).includes(q.id))||orla.ines;if(cm==='mq_04')return orla.cisternDoor}if(world==='cistern'){const cm=currentCampaignMission(),pr=progressMain();if(cm==='mq_04'){const v=cistern.valves.find(v=>!(pr.valves||[]).includes(v.id));if(v)return v;return goblins.find(g=>!g.dead)||cistern.exit}if(cm==='mq_05')return cistern.returnPortal}return null}
function arrowToTarget''','target function')

# Draw loop supports Orla and Cisterna.
sub(r"function draw\(\)\{.*?\}\nfunction label",r'''function draw(){ctx.clearRect(0,0,W,H);if(!player)return;const map=mapForWorld();cam.x=Math.max(0,Math.min(map.w-W,player.x-W/2));cam.y=Math.max(0,Math.min(map.h-H,player.y-H/2));ctx.save();ctx.translate(-cam.x,-cam.y);if(world==='city')drawCity();else if(world==='guild')drawGuild();else if(world==='orla')drawOrla();else if(world==='cistern')drawCistern();else drawCamp();drawPlayer();ctx.restore();arrowToTarget();drawAim();updateHint()}
function label''','draw function')

# Draw caravan in city.
s=s.replace("npc(1080,480,'Breno Carvalho','#9fa7b2',false)}","npc(1080,480,'Breno Carvalho','#9fa7b2',false);const cs=readCampaignMain();if(cs&&cs.unlocked){ctx.fillStyle='#69513b';ctx.fillRect(orlaDeparture.x-45,orlaDeparture.y-24,90,48);label('Caravana para Orla',orlaDeparture.x-65,orlaDeparture.y-36,'#f0d49a')}}",1)

# New map art and interactive markers.
insert_draw=r'''function drawOrla(){ctx.fillStyle='#2d3432';ctx.fillRect(0,0,orla.w,orla.h);ctx.fillStyle='#314b55';ctx.fillRect(0,690,orla.w,210);ctx.fillStyle='#3e3a34';for(let x=190;x<1420;x+=210){ctx.fillRect(x,90,145,125);ctx.fillStyle='#25282b';ctx.fillRect(x+20,120,38,48);ctx.fillRect(x+82,120,38,48);ctx.fillStyle='#3e3a34'}ctx.fillStyle='#5b4a39';ctx.fillRect(235,175,240,70);label('ABRIGO DA CISTERNA',260,165,'#ead8a8',15);npc(orla.saira.x,orla.saira.y,'Saira Vento','#c69173',currentCampaignMission()==='mq_01'||currentCampaignMission()==='mq_02');npc(orla.ines.x,orla.ines.y,'Inês Lume','#9c89b8',currentCampaignMission()==='mq_03');ctx.fillStyle='#29231f';ctx.fillRect(orla.cisternDoor.x-55,orla.cisternDoor.y-45,110,90);label('CISTERNA',orla.cisternDoor.x-35,orla.cisternDoor.y-56,'#d8c8a4');label('Retorno',orla.returnGate.x-28,orla.returnGate.y-45,'#ddd');const cm=currentCampaignMission(),pr=progressMain();if(cm==='mq_02')for(const r of orla.residents)if(!(pr.rescued||[]).includes(r.id)){npc(r.x,r.y,r.name,'#b8b0a1',true);ctx.strokeStyle='#6a90a2';ctx.beginPath();ctx.arc(r.x,r.y,42,0,Math.PI*2);ctx.stroke()}if(cm==='mq_03')for(const q of orla.clues)if(!(pr.clues||[]).includes(q.id)){ctx.fillStyle='#d6bd72';ctx.fillRect(q.x-12,q.y-12,24,24);label(q.name,q.x-45,q.y-22,'#ffe7a3')}}
function drawCistern(){ctx.fillStyle='#181c21';ctx.fillRect(0,0,cistern.w,cistern.h);ctx.fillStyle='#27303a';for(let x=80;x<1120;x+=160){ctx.fillRect(x,80,26,560);ctx.fillStyle='#4a4035';ctx.fillRect(x-12,210,50,18);ctx.fillStyle='#27303a'}label('SAÍDA',55,610,'#ddd');const cm=currentCampaignMission(),pr=progressMain();for(const v of cistern.valves){const done=(pr.valves||[]).includes(v.id);ctx.fillStyle=done?'#5d7f67':'#a36b4a';ctx.beginPath();ctx.arc(v.x,v.y,22,0,Math.PI*2);ctx.fill();label(done?'Válvula interrompida':'Válvula',v.x-45,v.y-32,done?'#9fd0aa':'#efc39c')}for(const g of goblins){if(g.dead)continue;if(g.state==='windup'){ctx.fillStyle='#d33a';ctx.beginPath();ctx.arc(g.attackX,g.attackY,58,0,Math.PI*2);ctx.fill();ctx.strokeStyle='#ff6565';ctx.stroke()}ctx.fillStyle='#86715e';ctx.beginPath();ctx.arc(g.x,g.y,g.r,0,Math.PI*2);ctx.fill();label('Síndico da Cisterna',g.x-70,g.y-42,'#f1d7ba',14);ctx.fillStyle='#222';ctx.fillRect(g.x-60,g.y+38,120,8);ctx.fillStyle='#b84b4b';ctx.fillRect(g.x-60,g.y+38,120*g.hp/g.maxHp,8)}if(cm==='mq_05'){portal(cistern.returnPortal.x,cistern.returnPortal.y);label('Retorno a Orla',cistern.returnPortal.x-48,cistern.returnPortal.y-55,'#ddd')}}
'''
s=s.replace('function drawCamp(){',insert_draw+'function drawCamp(){',1)

# Interaction hint for new NPCs/maps.
sub(r"function currentInteract\(\)\{.*?\}\nfunction updateHint",r'''function currentInteract(){if(!player)return'';if(world==='city'){if(near(city.guildDoor,82))return'Entrar na Guilda';if(near({x:470,y:500},78))return'Davi Moura';if(near({x:1080,y:480},78))return'Breno Carvalho';if(near(city.portal,82)&&mission===S.PORTAL)return'Portal Rank F';const cs=readCampaignMain();if(cs&&cs.unlocked&&near(orlaDeparture,82))return'Viajar para Orla'}if(world==='guild'){if(near(guild.exit,82))return'Sair da Guilda';if(near(guild.reception,78))return'Helena Duarte';if(near(guild.captain,78))return'Raul Vilar';if(near({x:520,y:290},76))return'Caio Nunes';if(near({x:570,y:360},76))return'Mirela Santos';if(near(guild.board,78))return'Quadro de Missões'}if(world==='orla'){const cm=currentCampaignMission(),pr=progressMain();if(near(orla.returnGate,82))return'Voltar à Cidade Inicial';if(near(orla.saira,78))return'Saira Vento';if(near(orla.ines,78))return'Inês Lume';if(cm==='mq_02'&&orla.residents.some(r=>!(pr.rescued||[]).includes(r.id)&&near(r,75)))return'Resgatar morador';if(cm==='mq_03'&&orla.clues.some(q=>!(pr.clues||[]).includes(q.id)&&near(q,75)))return'Investigar evidência';if(cm==='mq_04'&&near(orla.cisternDoor,90))return'Entrar na Cisterna'}if(world==='cistern'){const cm=currentCampaignMission(),pr=progressMain();if(cm==='mq_04'&&near(cistern.exit,82))return'Sair da Cisterna';if(cm==='mq_04'&&cistern.valves.some(v=>!(pr.valves||[]).includes(v.id)&&near(v,75)))return'Interromper válvula';if(cm==='mq_05'&&near(cistern.returnPortal,88))return'Retornar a Orla'}if(world==='camp'&&goblins.filter(g=>g.dead).length>=5&&near(camp.returnPortal,82))return'Portal de retorno';return''}
function updateHint''','currentInteract')

# Validate critical systems exist in final build.
for needle in ['Saira Vento','Síndico da Cisterna','Fragmento de Goblin','campaignReward','EXP ${player.xp||0}','Viajar para Orla']:
    if needle not in s:
        raise SystemExit(f'validation failed: {needle}')

p.write_text(s,encoding='utf-8')
