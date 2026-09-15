from pathlib import Path

src=Path('gameplay-patch-v072.py')
code=src.read_text(encoding='utf-8')
old="function mapForWorld(){return world==='city'?city:world==='guild'?guild:world==='orla'?orla:world==='cistern'?cistern:camp}\"\nrep(camp_line"
new="function mapForWorld(){return world==='city'?city:world==='guild'?guild:world==='orla'?orla:world==='cistern'?cistern:camp}\"\"\"\nrep(camp_line"
if old not in code:
    raise SystemExit('map string terminator not found')
code=code.replace(old,new,1)
compile(code,str(src),'exec')
exec(compile(code,str(src),'exec'))
