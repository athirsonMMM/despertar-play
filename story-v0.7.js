(()=>{
const CAMPAIGN_KEY='despertar-campaign-v071';
const slides=[
 {cls:'ruins',k:'PRÓLOGO • ANO ZERO',t:'O mundo caiu',p:'As primeiras criaturas atravessaram fendas que ninguém sabia explicar. Cidades inteiras desapareceram em poucos dias. Exércitos falharam, fronteiras ruíram e os sobreviventes passaram a viver entre muralhas improvisadas, ruínas e zonas abandonadas.'},
 {cls:'portal',k:'PRÓLOGO • AS FENDAS',t:'Então vieram os Portais',p:'Alguns levavam a territórios hostis. Outros despejavam monstros sobre a Terra. Cada portal passou a ser tratado como uma incursão: entrar, sobreviver, compreender suas regras e voltar antes que a passagem mudasse.'},
 {cls:'portal',k:'PRÓLOGO • O SISTEMA',t:'A humanidade despertou',p:'No limite da extinção, uma pequena parcela das pessoas passou a enxergar o Sistema. Força, magia, sentidos e habilidades impossíveis surgiram. Guerreiro, Mago, Arqueiro e Ladino tornaram-se as primeiras raízes conhecidas dos Despertos.'},
 {cls:'city',k:'PRÓLOGO • RECONSTRUÇÃO',t:'Guildas nasceram entre as ruínas',p:'Os Despertos passaram a proteger refúgios, explorar portais e recuperar território. As Guildas registram missões, ranques e incursões. Todo novato começa no Rank F. Antes de qualquer glória, é preciso provar que consegue voltar vivo.'},
 {cls:'orla',k:'ARCO I • ENTRE VÉUS',t:'O peso dos nomes',p:'Mas os monstros não são o único perigo. Na região de Orla, ruas, pessoas e registros começaram a desaparecer sem desaparecer da memória de todos. Algo nas Dobras está alterando a realidade. A sua primeira grande campanha começa depois da prova Rank F.'}
];

const chapters=[
 {n:1,title:'A rua que bebeu o próprio nome',place:'Orla e a Cisterna',levels:'1–5',boss:'Síndico da Cisterna',reveal:'A Testemunha é uma condição compartilhável, não um herói único.',missions:[
  ['mq_01','Filtros antes de glória','Leve uma caixa de filtros de água até o abrigo da Cisterna em Orla. Fale com Saira, ajude a distribuir suprimentos e descubra por que uma rua está ausente dos mapas.'],
  ['mq_02','Quem ficou na água','Entre na zona alagada, encontre três moradores presos e use pontos de ancoragem para retirá-los antes que o nível da água suba.'],
  ['mq_03','Uma placa, duas ruas','Investigue a placa recuperada, compare o mapa atual com o mapa antigo de Inês e identifique três inconsistências sem escolher qual memória é a verdadeira.'],
  ['mq_04','O fundo responde','Desça à Cisterna, interrompa as válvulas que alimentam o padrão e derrote o Síndico da Cisterna. Recupere a inscrição com o nome Namar.']
 ]},
 {n:2,title:'O pedágio dos ausentes',place:'Estrada das Lanternas',levels:'6–10',boss:'O Cobrador',reveal:'O apagamento produzia benefício econômico.',missions:[
  ['mq_05','Carta sem destinatário','Escolte Lio com os remédios até a primeira cancela e descubra por que a estrada exige nomes de pessoas que não constam nos registros.'],
  ['mq_06','Três luzes acesas','Reative três lanternas de orientação, defendendo cada posto contra criaturas atraídas pelos selos de pedágio.'],
  ['mq_07','A soma dos passageiros','Recupere manifestos de caravanas e prove que passageiros foram registrados como mercadoria para sustentar cobranças falsas.'],
  ['mq_08','Passagem contestada','Enfrente O Cobrador, que transforma recibos e nomes em correntes, e entregue à Liga dois manifestos públicos: bens e pessoas.']
 ]},
 {n:3,title:'O turno que não acabou',place:'Pedreiras de Âmbar',levels:'11–15',boss:'Capataz de Horas',reveal:'A Trama consome trabalho e identidade, não apenas lembranças.',missions:[
  ['mq_09','Livro de pagamento','Investigue o livro de pagamentos, confronte turnos ausentes e identifique trabalhadores retirados do registro oficial.'],
  ['mq_10','Freio de emergência','Desative prensas e correias em três setores antes que as máquinas repitam o turno fatal.'],
  ['mq_11','Última descida','Desça pelo elevador clandestino, localize trabalhadores presos e abra uma rota segura de retorno.'],
  ['mq_12','O relógio do capataz','Derrote o Capataz de Horas e recupere o relógio-registro que liga o âmbar às caldeiras da cidade.']
 ]},
 {n:4,title:'As raízes que assinam',place:'Jardim Suspenso',levels:'16–20',boss:'Jardineira Enxertada',reveal:'Consentimento tem escopo; uma assinatura não autoriza gerações inteiras.',missions:[
  ['mq_13','A colheita assinada','Ajude Nara a colher amostras e encontre nomes humanos crescendo nas fibras de plantas alteradas.'],
  ['mq_14','Permissão não herdada','Localize o contrato original da família e prove que uma doação voluntária foi ampliada para descendentes sem consentimento.'],
  ['mq_15','Sementes de amanhã','Proteja três lotes de sementes independentes enquanto o jardim reage à separação do protocolo.'],
  ['mq_16','Podar o comando','Separe raízes de alimento das raízes de comando e derrote a Jardineira Enxertada sem destruir a produção inteira.']
 ]},
 {n:5,title:'A margem do arquivo',place:'Arquivo de Vidro',levels:'21–25',boss:'Índice Vivo',reveal:'Inês participou do apagamento e a descoberta não a absolve.',missions:[
  ['mq_17','A borda arrancada','Entre no Arquivo de Vidro e reconstrua páginas de mapas onde a sétima cidade foi removida das margens.'],
  ['mq_18','A assinatura de Inês','Confronte Inês com a revisão cartográfica assinada por ela e reúna o relatório que motivou a exclusão.'],
  ['mq_19','Cópias fora do cofre','Crie e distribua três cópias do decreto, protegendo dados pessoais dos anexos privados.'],
  ['mq_20','O índice devora','Derrote o Índice Vivo antes que ele destrua todas as referências a Namar e recupere o manifesto do navio.']
 ]},
 {n:6,title:'O navio que chegou tarde',place:'Mar de Baixo',levels:'26–30',boss:'Almirante da Vazante',reveal:'Ecos não são sobreviventes e não prometem ressurreição.',missions:[
  ['mq_21','Cabines repetidas','Explore o navio revelado pela vazante e marque cabines que continham pessoas vivas no instante do apagamento.'],
  ['mq_22','Cordas da vazante','Prenda o casco em quatro pontos antes que a maré arraste o navio para a costa.'],
  ['mq_23','A última carta','Encontre o registro final do irmão de Dora e leve a mensagem sem alterar o que realmente aconteceu.'],
  ['mq_24','Atracação impossível','Derrote o Almirante da Vazante e recupere a chave de Iri que permite acesso estável a Namar.']
 ]},
 {n:7,title:'A segunda manhã',place:'Namar Devolvida',levels:'31–35',boss:'Sentinela do Endereço',reveal:'Namar contém pessoas vivas e uma sociedade que continuou existindo por dentro.',missions:[
  ['mq_25','Primeiro, água','Ajude Véspera a montar pontos de água e abrigo antes de iniciar qualquer disputa política.'],
  ['mq_26','Duas chaves, uma casa','Medie o primeiro conflito de propriedade entre um morador de Namar e um ocupante atual de Orla.'],
  ['mq_27','O nome de Lio','Acompanhe Lio ao reencontro com alguém que conheceu sua família e revele que ele próprio é um Retornado.'],
  ['mq_28','Ninguém é duplicata','Derrote a Sentinela do Endereço e libere a emissão de documentos provisórios para os Retornados.']
 ]},
 {n:8,title:'Quem pode testemunhar',place:'Tribunal das Ausências',levels:'36–40',boss:'Notário de Cinza',reveal:'Prova não exige violar intimidade nem impor uma memória oficial.',missions:[
  ['mq_29','Direito de recusar','Reúna depoimentos voluntários e estabeleça que nenhuma pessoa precisa expor lembranças íntimas para provar cidadania.'],
  ['mq_30','A negativa antiga','Recupere o processo em que Raul negou o mesmo direito à mãe de Lio e faça o tribunal reconhecer a contradição.'],
  ['mq_31','Duas testemunhas','Proteja duas testemunhas independentes até a audiência e registre versões diferentes do mesmo evento sem apagar nenhuma.'],
  ['mq_32','O carimbo final','Derrote o Notário de Cinza e escolha entre restituição documental rápida ou comissão comunitária com recurso.']
 ]},
 {n:9,title:'Calor sem esquecimento',place:'Forja do Inverno',levels:'41–45',boss:'Coração de Escória',reveal:'Existe alternativa material testável ao apagamento.',missions:[
  ['mq_33','A planta incompleta','Reúna fragmentos das gravações de Iri e monte a planta do Protocolo de Restituição.'],
  ['mq_34','Três apoios','Instale três âncoras piloto em locais escolhidos com consentimento da população.'],
  ['mq_35','Uma noite de teste','Mantenha um bairro aquecido durante uma noite inteira, reparando falhas e defendendo as âncoras.'],
  ['mq_36','A forja resiste','Derrote o Coração de Escória e estabilize a pressão sem restaurar o antigo sistema de extração.']
 ]},
 {n:10,title:'As seis portas',place:'Cinturão das Seis Portas',levels:'46–50',boss:'Marechal dos Lacres',reveal:'Cooperação permite escala sem depender de todos os jogadores estarem online.',missions:[
  ['mq_37','Mapa de retirada','Planeje uma rota de evacuação com Saira e marque três pontos seguros de encontro.'],
  ['mq_38','A ordem falsa','Descubra qual ordem de resgate foi adulterada antes que equipes sejam enviadas para uma emboscada.'],
  ['mq_39','Voltar por eles','Retorne a uma zona já evacuada para buscar sobreviventes que ficaram presos após o fechamento de uma rota.'],
  ['mq_40','Lacres partidos','Derrote o Marechal dos Lacres e torne a rota de evacuação uma passagem permanente da região.']
 ]},
 {n:11,title:'A conta do regente',place:'Meridiano Partido',levels:'51–55',boss:'Auditor de Nomes',reveal:'Conhecer todas as vítimas não dá autoridade para escolher quem deve ser sacrificado.',missions:[
  ['mq_41','O custo declarado','Entre no Meridiano e reúna os registros que Oren usa para justificar o sacrifício de Namar.'],
  ['mq_42','A alternativa existe','Apresente os resultados da Forja estabilizada e prove que o apagamento não é tecnicamente inevitável.'],
  ['mq_43','Saída em comum','Abra a rota de retirada enquanto Inês mantém o acesso estável e impeça o fechamento do grupo dentro do Meridiano.'],
  ['mq_44','Sem chave de confisco','Derrote o Auditor de Nomes e retire da rede a chave que permite confiscar identidades e âncoras.']
 ]},
 {n:12,title:'O peso dos nomes',place:'Praça do Pacto',levels:'56–60',boss:'Conta Infinda',reveal:'O ciclo local de apagamento termina, mas reconstrução e política continuam.',missions:[
  ['mq_45','A mesa incompleta','Reúna representantes das facções e garanta que Namar tenha assento antes da abertura do pacto.'],
  ['mq_46','Lastro repartido','Distribua a carga da Trama entre as âncoras construídas ao longo da campanha e defenda cada ligação.'],
  ['mq_47','Nenhum nome a mais','Recuse o sacrifício individual exigido pela Conta Infinda e interrompa as ordens finais de confisco.'],
  ['mq_48','O primeiro dia seguinte','Finalize o Pacto, escolha seu legado — Rotas, Memória ou Ofícios — e receba a carta da oitava costa.']
 ]}
];

function readCampaign(){try{return JSON.parse(localStorage.getItem(CAMPAIGN_KEY)||'null')}catch{return null}}
function writeCampaign(s){localStorage.setItem(CAMPAIGN_KEY,JSON.stringify(s))}
function ensureCampaign(){let s=readCampaign();if(!s){s={chapter:1,mission:'mq_01',completed:[],unlocked:true};writeCampaign(s)}return s}
function allMissions(){return chapters.flatMap(c=>c.missions.map(m=>({chapter:c.n,id:m[0],title:m[1],desc:m[2]})))}
function missionById(id){return allMissions().find(m=>m.id===id)}
function unlockCampaign(){const s=ensureCampaign();s.unlocked=true;s.chapter=1;if(!s.mission)s.mission='mq_01';writeCampaign(s);showUnlockToast()}
function showUnlockToast(){let t=document.getElementById('campaignUnlockToast');if(!t){t=document.createElement('div');t.id='campaignUnlockToast';t.style.cssText='position:absolute;z-index:60;left:50%;top:82px;transform:translateX(-50%);background:#101722ee;border:1px solid #d8ad58;color:#fff;padding:12px 16px;border-radius:8px;box-shadow:0 8px 30px #0008;text-align:center;max-width:80%';document.getElementById('wrap')?.appendChild(t)}const m=missionById(readCampaign()?.mission||'mq_01');t.innerHTML=`<b>NOVA MISSÃO PRINCIPAL</b><br>${m?.title||'Filtros antes de glória'}`;t.style.display='block';clearTimeout(t._h);t._h=setTimeout(()=>t.style.display='none',4200)}
window.addEventListener('despertar:campaign-unlock',unlockCampaign);

const css=document.createElement('link');if(!document.querySelector('link[href="story-v0.7.css"]')){css.rel='stylesheet';css.href='story-v0.7.css';document.head.appendChild(css)}
const wrap=document.getElementById('wrap');if(!wrap)return;
const badge=document.createElement('div');badge.className='story-title-badge';badge.textContent='CAMPANHA • ENTRE VÉUS';wrap.appendChild(badge);
const btn=document.createElement('button');btn.id='storyBtn';btn.textContent='📖 HISTÓRIA';wrap.appendChild(btn);
const ov=document.createElement('div');ov.className='story-overlay';ov.innerHTML='<div class="story-card"><button class="story-close" aria-label="Fechar">×</button><div id="storyMount"></div></div>';wrap.appendChild(ov);
const mount=ov.querySelector('#storyMount');const close=()=>ov.classList.remove('open');ov.querySelector('.story-close').onclick=close;ov.addEventListener('click',e=>{if(e.target===ov)close()});
let introI=0;
function openIntro(fromMenu=false){introI=0;ov.dataset.mode=fromMenu?'intro-menu':'intro-new';renderIntro();ov.classList.add('open')}
function renderIntro(){const s=slides[introI];mount.innerHTML=`<div class="story-hero ${s.cls}"><div class="story-hero-content"><div class="story-kicker">${s.k}</div><h2>${s.t}</h2><p>${s.p}</p><div class="story-dots">${slides.map((_,i)=>`<i class="story-dot ${i===introI?'on':''}"></i>`).join('')}</div></div></div><div class="story-body"><div class="story-actions"><button class="story-action" id="storyPrev" ${introI===0?'disabled':''}>Voltar</button><button class="story-action primary" id="storyNext">${introI===slides.length-1?'Continuar para criação':'Próximo'}</button></div></div>`;mount.querySelector('#storyPrev').onclick=()=>{if(introI>0){introI--;renderIntro()}};mount.querySelector('#storyNext').onclick=()=>{if(introI<slides.length-1){introI++;renderIntro();return}close();if(ov.dataset.mode==='intro-new'){document.getElementById('menuScreen').style.display='none';document.getElementById('createScreen').style.display='flex'}}}
function readSave(){try{return JSON.parse(localStorage.getItem('despertar-v071-save')||localStorage.getItem('despertar-v070-save')||'null')}catch{return null}}
function tutorialDone(){const s=readSave();return !!(s&&s.mission==='done')}
function campaignStatus(){const s=readCampaign();return s||{chapter:1,mission:'mq_01',completed:[],unlocked:tutorialDone()}}
function openChapters(){const cs=campaignStatus(),unlocked=cs.unlocked||tutorialDone();mount.innerHTML=`<div class="story-hero orla"><div class="story-hero-content"><div class="story-kicker">DESPERTAR • CAMPANHA PRINCIPAL</div><h2>Entre Véus — O peso dos nomes</h2><p>12 capítulos, 48 missões principais e uma progressão contínua após sua primeira incursão Rank F.</p></div></div><div class="story-body"><div class="lore-box"><b>${unlocked?'Campanha liberada':'Campanha bloqueada'}</b><br>${unlocked?`Missão atual: ${missionById(cs.mission)?.title||'Filtros antes de glória'}`:'Conclua a missão dos Goblins, entregue a prova a Lívia Avelar e fale com o Capitão Caio Ferraz.'}</div><div class="chapter-list" style="margin-top:14px">${chapters.map(c=>`<div class="chapter ${unlocked&&c.n<=cs.chapter?'unlocked':'locked'}" data-i="${c.n-1}"><small>CAPÍTULO ${String(c.n).padStart(2,'0')} • Nv. ${c.levels}</small><b>${c.title}</b><span>${c.place}</span></div>`).join('')}</div><div id="chapterDetail" class="chapter-detail"></div><div class="story-note">Todos os capítulos e missões já estão definidos. A implementação jogável será conectada em ordem para não quebrar a base de movimentação e combate.</div></div>`;mount.querySelectorAll('.chapter').forEach(el=>el.onclick=()=>showChapter(+el.dataset.i,cs));showChapter(Math.max(0,(cs.chapter||1)-1),cs);ov.classList.add('open')}
function showChapter(i,cs){const d=mount.querySelector('#chapterDetail');if(!d)return;const c=chapters[i],active=cs.mission;d.innerHTML=`<h3>Capítulo ${String(c.n).padStart(2,'0')} — ${c.title}</h3><div class="lore-box"><b>Local:</b> ${c.place} • <b>Faixa sugerida:</b> ${c.levels}<br><b>Boss:</b> ${c.boss}<br><b>Revelação:</b> ${c.reveal}</div>${c.missions.map(m=>`<div class="quest-row"><b>${m[0]} • ${m[1]}${active===m[0]?' • MISSÃO ATUAL':''}</b><span>${m[2]}</span></div>`).join('')}<div class="story-actions">${c.n===1?'<button class="story-action" id="previewScene">Ver cena de abertura</button>':''}</div>`;const pv=d.querySelector('#previewScene');if(pv)pv.onclick=previewChapterOne}
function previewChapterOne(){mount.innerHTML=`<div class="story-hero orla"><div class="story-hero-content"><div class="story-kicker">CAPÍTULO 01 • ORLA</div><h2>A rua que bebeu o próprio nome</h2><p>A chuva parou, mas a água na cisterna continua subindo. No mapa de Inês, a rua termina antes da praça. Na memória de uma moradora, existe uma casa depois dela. Você consegue lembrar das duas coisas ao mesmo tempo.</p></div></div><div class="story-body"><div class="story-npc"><div class="story-portrait">🗺</div><div><b>Inês Lume</b><div class="story-note">“Não tente decidir agora qual lembrança é a verdadeira. Primeiro tire as pessoas da água.”</div></div></div><div class="story-npc"><div class="story-portrait">⚔</div><div><b>Saira Vento</b><div class="story-note">“Três moradores ainda estão lá embaixo. Cordas primeiro. Perguntas depois.”</div></div></div><div class="story-actions"><button class="story-action primary" id="backChapters">Voltar aos capítulos</button></div></div>`;mount.querySelector('#backChapters').onclick=openChapters}
btn.onclick=openChapters;
const nb=document.getElementById('newBtn');if(nb)nb.onclick=()=>openIntro(false);
const menu=document.getElementById('menuScreen');if(menu){const p=menu.querySelector('.panel .row');if(p){const lore=document.createElement('button');lore.className='btn';lore.textContent='Prólogo';lore.onclick=()=>openIntro(true);p.appendChild(lore)}}
if(tutorialDone()&&!readCampaign())unlockCampaign();
})();