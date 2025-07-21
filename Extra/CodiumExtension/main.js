const [vs,fs] = ["vscode","fs"].map(require);

const ζ = (...𝔸)=>[...𝔸[0]].map((_,i)=>𝔸.map(x=>x[i]));
const ᔐ𝑙 = x=>[...x].length;
const [𝒪ℒ,ℒ𝒪] = [Object.entries,Object.fromEntries];
const 𝒪ℳ = x=>x.reduce((x,y)=>({...x,...y}))
const rmat = f=>fs.readFileSync(f, {encoding:'utf8', flag:'r'}).split('\n').map(x=>[...x]);
const print = (...𝔸) => console.log(...𝔸) || 𝔸[0];
Number.prototype.mod = function(n) { return (this%n + n)%n; };

const 𝔖𝔏 = 𝚜=>[𝚜.start.line,𝚜.start.character,𝚜.end.line,𝚜.end.character];
const 𝔏𝔖 = (αl,αc,βl,βc)=>new vs.Selection(new vs.Position(αl,αc),new vs.Position(βl,βc));

MOON_PATH = require('child_process').execSync('☾ --get-dir').toString().trim();
SCRP_PATH = `${MOON_PATH}/Builtins/Data/script.map`;
ORDR_PATH = `${MOON_PATH}/Builtins/Data/opord`;

const mapS = (_=>{
    const odat     = rmat(ORDR_PATH);
    const N        = odat.length-1;
    const oadt     = ζ(...odat);
    const order    = 𝒪ℳ(odat.map((x,i)=>ℒ𝒪(x.map(x=>[x,i]))));
    const expand   = ℒ𝒪(oadt.map(([x,...𝔸])=>[x,𝔸]));
    const contract = 𝒪ℳ(𝒪ℒ(expand).map(([k,v])=>ℒ𝒪(v.map(x=>[x,k]))));
    const loc      = x=>x in contract ?[contract[x],order[x]]: undefined;
    const col      = (x,Δ=0,c=0)=>expand[x[0]][c==1 ? Math.min(Math.max(x[1]+Δ-1,0),N-1):
                                               c<0  ? -c:
                                               (x[1]+Δ-1)%N];
    
    return (S,...𝔸)=>[...S].map(x => x in contract ?col(loc(x),...𝔸):
                                     x in expand   ?expand[x][Math.floor(expand[x].length/2)]:
                                     x).join(''); })();

const [SUP,SUB,NRM] = [{},{},{}];
for(const [n,p,b] of ζ(...rmat(SCRP_PATH))) {
    [SUP[n],SUB[n]] = [p,b];
    NRM[b] = NRM[p] = n; }

const part = (s,i) => [s.slice(0,i),s.slice(i)];
const align = 𝐸 => {
    const gl = l=>𝐸.document.lineAt(l);
    const L = 𝐸.selections.map(𝔖𝔏).map(([αl,αc,βl,βc]) => [αl,αc,...part(gl(αl).text,αc)]);
    const n = Math.max(...L.map(([l,c,α,β]) => ᔐ𝑙(α)));
    const ns = [];
    𝐸.edit(𝑒𝑏=>
        L.forEach(([l,c,α,β])=>
            (𝑒𝑏.replace(new vs.Range(l,0,l,𝐸.document.lineAt(l).text.length),
                       α+' '.repeat(n-ᔐ𝑙(α))+β),
             ns.push(𝔏𝔖(l,α.length+n-ᔐ𝑙(α),l,α.length+n-ᔐ𝑙(α))))))
     .then(_=>𝐸.selections=ns) };
align.manual = true;

const tools = {   sup: s=>[...s].map(c=>SUP[c]??c).join(''),
                  sub: s=>[...s].map(c=>SUB[c]??c).join(''),
                  nrm: s=>[...s].map(c=>NRM[c]??c).join(''),
                 ord1: s=>mapS(s, 1,  1),
                 dro1: s=>mapS(s,-1,  1),
                 ord3: s=>mapS(s, 3,  1),
                 dro3: s=>mapS(s,-3,  1),
                 set3: s=>mapS(s, 0,- 3),
                set10: s=>mapS(s, 0,-10),
                set17: s=>mapS(s, 0,-17),
                align }
// 󰤱 generalized upper/lower/swapcase, switching alphabets

const fc = (𝐸,l,c) => [l,ᔐ𝑙(part(    𝐸.document.lineAt(l).text, c)[0])                ];
const cf = (𝐸,l,c) => [l,   part([...𝐸.document.lineAt(l).text],c)[0] .join('').length];
const tin = (𝐸,𝚜,ƒ) => { 𝚜 = ƒ( [...fc(𝐸,𝚜[0],𝚜[1]),...fc(𝐸,𝚜[2],𝚜[3])]);
                         return [...cf(𝐸,𝚜[0],𝚜[1]),...cf(𝐸,𝚜[2],𝚜[3]) ]; }
const a1 = (𝐸,𝚜) => tin(𝐸,𝚜,𝚜=>[𝚜[0],𝚜[1],𝚜[2],𝚜[3]+1]);
const nzSel = (𝐸,𝚜) => (𝚜=>𝔏𝔖(...𝚜[0]==𝚜[2]&&𝚜[1]==𝚜[3] ?a1(𝐸,𝚜): [𝚜[0],𝚜[1],𝚜[2],𝚜[3]]))(𝔖𝔏(𝚜));
const activate = ℭ =>
    Object.entries(tools).map(([k,v])=>
        vs.commands.registerCommand(`moon.${k}`, _=>{
            const 𝐸 = vs.window.activeTextEditor;
            if(v.manual) v(𝐸);
            else         𝐸.edit(𝑒𝑏 => 𝐸.selections.map(𝚜 => nzSel(𝐸,𝚜))
                                       .forEach(𝚜 => 𝑒𝑏.replace(𝚜,v(𝐸.document.getText(𝚜))))); })
    ).forEach(ℭ.subscriptions.push);
const deactivate = _ => {};

module.exports = { activate, deactivate };