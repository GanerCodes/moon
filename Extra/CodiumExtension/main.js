const [vs,fs] = ["vscode","fs"].map(require);

const ζ = (...𝔸)=>[...𝔸[0]].map((_,i)=>𝔸.map(x=>x[i]));
const ᔐ𝑙 = x=>[...x].length;
const [𝒪ℒ,ℒ𝒪] = [Object.entries,Object.fromEntries];
const 𝒪ℳ = x=>x.reduce((x,y)=>({...x,...y}))
const rmat = f=>fs.readFileSync(f, {encoding:'utf8', flag:'r'}).split('\n').map(x=>[...x]);
Number.prototype.mod = function(n) { return (this%n + n)%n; };

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
    const col      = (x,Δ=0,c=false)=>expand[x[0]][c?Math.min(Math.max(x[1]+Δ-1,0),N-1):(x[1]+Δ-1)%N];
    return (S,...𝔸)=>[...S].map(x=>x in contract ?col(loc(x),...𝔸): x).join(''); })();

const [SUP,SUB,NRM] = [{},{},{}];
for(const [n,p,b] of ζ(...rmat(SCRP_PATH))) {
    [SUP[n],SUB[n]] = [p,b];
    NRM[b] = NRM[p] = n; }

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

const tools = {  sup: s=>[...s].map(c=>SUP[c]??c).join(''),
                 sub: s=>[...s].map(c=>SUB[c]??c).join(''),
                 nrm: s=>[...s].map(c=>NRM[c]??c).join(''),
                ord1: s=>mapS(s, 1,true),
                dro1: s=>mapS(s,-1,true),
                ord5: s=>mapS(s, 5,true),
                dro5: s=>mapS(s,-5,true),
                align }
// 󰤱 generalized upper/lower/swapcase, switching alphabets

const activate = ℭ => 
    Object.entries(tools).map(([k,v])=>
        vs.commands.registerCommand(`moon.${k}`, _=>{
            const 𝐸 = vs.window.activeTextEditor;
            if(v.manual) v(𝐸);
            else         𝐸.edit(𝑒𝑏 => 𝐸.selections.forEach(𝚜 => 𝑒𝑏.replace(𝚜,v(𝐸.document.getText(𝚜))))); })
    ).forEach(ℭ.subscriptions.push);
const deactivate = _ => {};

module.exports = { activate, deactivate };