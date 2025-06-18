const vs = require('vscode');
const fs = require('fs');
const { execSync } = require('child_process');

MOON_PATH = execSync('☾ --get-dir').toString().trim();
const ζ = (...𝔸)=>[...𝔸[0]].map((_,i)=>𝔸.map(x=>x[i]));
const CHARLISTS = fs.readFileSync(`${MOON_PATH}/FontCompose/.SCRIPT_MAP`,
        {encoding: 'utf8', flag: 'r'}).split('\n').map(x=>[...x]);
const [SUP,SUB,NRM] = [{},{},{}];
for(const [n,p,b] of ζ(...CHARLISTS)) {
    [SUP[n],SUB[n]] = [p,b];
    NRM[b] = NRM[p] = n; }

const ᔐ𝑙 = x=>[...x].length;
const part = (s,i) => [s.slice(0,i),s.slice(i)];
const align = 𝐸 => {
    const gl = l=>𝐸.document.lineAt(l);
    const L = 𝐸.selections.map(𝚜 => [𝚜.start.line, 𝚜.start.character,
                                     ...part(gl(𝚜.start.line).text,
                                             𝚜.start.character)]);
    const n = Math.max(...L.map(([l,c,α,β]) => ᔐ𝑙(α)));
    const ns = [];
    𝐸.edit(𝑒𝑏=>
        L.forEach(([l,c,α,β])=>
            (𝑒𝑏.replace(new vs.Range(l,0,l,𝐸.document.lineAt(l).text.length),
                       α+' '.repeat(n-ᔐ𝑙(α))+β),
             ns.push(new vs.Selection(new vs.Position(l,α.length+n-ᔐ𝑙(α)),
                                      new vs.Position(l,α.length+n-ᔐ𝑙(α)))))))
     .then(_=>𝐸.selections=ns) };
align.manual = true;

const tools = { sup: s=>[...s].map(c=>SUP[c]??c).join(''),
                sub: s=>[...s].map(c=>SUB[c]??c).join(''),
                nrm: s=>[...s].map(c=>NRM[c]??c).join(''),
                align }
// 󰤱 generalized upper/lower/swapcase, switching op orders, switching alphabets

const activate = ℭ => 
    Object.entries(tools).map(([k,v])=>
        vs.commands.registerCommand(`moon.${k}`, _=>{
            const 𝐸 = vs.window.activeTextEditor;
            if(v.manual) v(𝐸);
            else         𝐸.edit(𝑒𝑏 => 𝐸.selections.forEach(𝚜 => 𝑒𝑏.replace(𝚜,v(𝐸.document.getText(𝚜))))); })
    ).forEach(ℭ.subscriptions.push);
const deactivate = _ => {};

module.exports = { activate, deactivate };