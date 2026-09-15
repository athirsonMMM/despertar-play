from pathlib import Path
p=Path('_site/story-v0.7.js')
s=p.read_text(encoding='utf-8')
s=s.replace('12 capítulos, 48 missões principais e uma progressão contínua após sua primeira incursão Rank F.','A campanha foi planejada em 12 capítulos. Nesta fase, os Capítulos 1–4 estão jogáveis; os Capítulos 5–12 ficam reservados para atualizações futuras enquanto o desenvolvimento prioriza as mecânicas de MMORPG.')
s=s.replace("unlocked&&c.n<=cs.chapter?'unlocked':'locked'","unlocked&&c.n<=Math.min(cs.chapter,4)?'unlocked':'locked'")
s=s.replace('Todos os capítulos e missões já estão definidos. Os Capítulos 1 e 2 já possuem sequência jogável; os seguintes serão conectados em ordem sem quebrar a base de movimentação e combate.','Capítulos 1–4 jogáveis. Capítulos 5–12 ficam reservados para uma atualização futura. A prioridade de desenvolvimento agora é combate, habilidades, progressão, base, economia, NPCs, IA e sistemas online.')
old="function showChapter(i,cs){const d=mount.querySelector('#chapterDetail');if(!d)return;const c=chapters[i],active=cs.mission;d.innerHTML=`<h3>Capítulo ${String(c.n).padStart(2,'0')} — ${c.title}</h3>"
new="function showChapter(i,cs){const d=mount.querySelector('#chapterDetail');if(!d)return;const c=chapters[i],active=cs.mission;if(c.n>4){d.innerHTML=`<h3>Capítulo ${String(c.n).padStart(2,'0')} — Conteúdo futuro</h3><div class=\"lore-box\"><b>Planejado para atualização futura.</b><br>Por enquanto o desenvolvimento está concentrado nas mecânicas centrais do MMORPG.</div>`;return}d.innerHTML=`<h3>Capítulo ${String(c.n).padStart(2,'0')} — ${c.title}</h3>"
if old not in s:
    raise SystemExit('showChapter marker not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
