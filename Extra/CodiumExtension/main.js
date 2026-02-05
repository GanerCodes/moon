const Ų = undefined;
const ζ = (...𝔸)=>𝔸.s(x=>x.length).at(-1).ᴍ((_,i)=>𝔸.ᴍ(x=>x[i]));
const ꟿ = (x,y,...𝔸)=>[...x].ᴍ((x,...𝔸)=>y(...x)); // 󰤱 we throw out 𝔸's, fix that but make sure it doesn't break anything
const pairs = (v) => v.toSpliced(-1,1).ᴍ((x,i)=>[x,v[i+1]]);
const ᔐ𝑙 = x=>[...x].length;
const 𝒪ℳ = x=>x.reduce((x,y)=>({...x,...y}))
const rmat = f=>fs.readFileSync(f, {encoding:'utf8', flag:'r'}).split('\n').ᴍ(x=>[...x]);
const log = (...𝔸) => console.log(...𝔸) || 𝔸[0];
const [𝒪𝒱,𝒪ℒ,ℒ𝒪] = [Object.values,Object.entries,Object.fromEntries];
const 𝔓 = x=>x.prototype;
𝔓(Number).mod  = function(   n) { return (this%n + n)%n; };
𝔓(Array).pairs = function(...𝔸) { return pairs(this,...𝔸); };
𝔓(Array).f     = function(...𝔸) { return this.filter(...𝔸); };
𝔓(Array).s     = function(   ƒ) { ƒ ??= x=>x;
                                  return this.toSorted((a,b)=>ƒ(a)-ƒ(b)); };
𝔓(Array).ᴍ     = function(...𝔸) { return this.map(...𝔸); };
𝔓(Array).ꟿ     = function(...𝔸) { return ꟿ(this,...𝔸); };
𝔓(Array).ζ     = function(    ) { return ζ(...this); };
𝔓(Array).max   = function(    ) { return Math.max(...this); };
𝔓(Array).G     = function(   ƒ) { O = {};
                                  this.forEach((x,...𝔸)=>(y=>y in O ?O[y].push(x): (O[y]=[x]))
                                                         (ƒ(x,...𝔸)));
                                  return O; };

const path = require("path");
const { exec, execSync } = require("child_process");
const [vs,fs] = ["vscode","fs"].ᴍ(require);

const getSpacing = curs => {
  const V = curs.ᴍ(x=>x[1]).ᴍ(x=>[x[0], ...x.pairs().ꟿ((a,b)=>b-a)]).ζ();
  const O = ζ(V, V.ᴍ(x=>x.f(x=>x!==Ų).max())).ꟿ((l,r) => l.ᴍ(x=>x !== Ų ?r-x: Ų));
  return ζ(curs.ᴍ(x=>x[0]), O.ζ().ᴍ(x=>x.f(x=>x!==Ų))); }

const 𝔖𝔏 = 𝚜=>[𝚜.start.line,𝚜.start.character,𝚜.end.line,𝚜.end.character];
const 𝔏𝔖 = (αl,αc,βl,βc)=>new vs.Selection(new vs.Position(αl,αc),new vs.Position(βl,βc));

const highlights = [
    [/(?<=␛)./gu, { color:"#22ff22", backgroundColor:"#006600aa" }],
    [/ /gu      , { backgroundColor:"#ffff0044", borderWidth:"1px",
                    borderStyle:"solid", borderColor:"#ff0" }],
    [/ /gu      , { backgroundColor:"#0000ff66", borderWidth:"1px",
                    borderStyle:"solid", borderColor:"#00f" }]
];
highlights.forEach(x => x[1] = vs.window.createTextEditorDecorationType(x[1]));

let mapS;
const [SUP,SUB,NRM] = [{},{},{}];
try{
  const isWin = process.platform === 'win32';
  MOON_PATH = execSync(isWin ? 'wsl -e /usr/bin/env bash -c "$HOME/.local/bin/☾ --get-dir"'
                             : '☾ --get-dir'
                      ).toString().trim();
  if(isWin) MOON_PATH = MOON_PATH.replace(/^\/mnt\/([a-z])/, (_,d)=>`${d.toUpperCase()}:`);
  SCRP_PATH = `${MOON_PATH}/Builtins/Data/script.map`;
  ORDR_PATH = `${MOON_PATH}/Builtins/Data/opord`;
  mapS = (_=>{
      const odat     = rmat(ORDR_PATH);
      const N        = odat.length-1;
      const oadt     = ζ(...odat);
      const order    = 𝒪ℳ(odat.ᴍ((x,i)=>ℒ𝒪(x.ᴍ(x=>[x,i]))));
      const expand   = ℒ𝒪(oadt.ᴍ(([x,...𝔸])=>[x,𝔸]));
      const contract = 𝒪ℳ(𝒪ℒ(expand).ᴍ(([k,v])=>ℒ𝒪(v.ᴍ(x=>[x,k]))));
      const loc      = x=>x in contract ?[contract[x],order[x]]: Ų;
      const col      = (x,Δ=0,c=0)=>expand[x[0]][c==1 ? Math.min(Math.max(x[1]+Δ-1,0),N-1):
                                                 c<=0 ? -c:
                                                 (x[1]+Δ-1)%N];
      
      return (S,...𝔸)=>[...S].ᴍ(x => x in contract ?col(loc(x),...𝔸):
                                     x in expand   ?expand[x][Math.floor(expand[x].length/2)]:
                                     x).join(''); })();

  for(const [n,p,b] of ζ(...rmat(SCRP_PATH))) {
      [SUP[n],SUB[n]] = [p,b];
      NRM[b] = NRM[p] = n; }
}catch(ε){ log("Error doing ☾ stuff!",ε); }

const part = (s,i) => [s.slice(0,i),s.slice(i)];
const align = 𝐸 => {
  /*
  curs = [[3,[1,5]],
        [5,[3,4,9]],
        [8,[6]],
        [9,[0,1,2,3,4]]]
  V = cursᐵ₁ᐸᐵ₀ 􀞚 ⟞􀊀₀󰄎₁􀉴􀁘ᵜᐸ 􀋅􋄅
  O = V ᐵᐵ􇪨􇃆⟞􀊪ᵜᑅᑈ (Vᐵ􀉻􇪥􀋯ᐸ)
  H = cursᐵ₀ᐸ􀠊O􀋅􋄅
  H􀉴􀁦
  */
  let [𝔩,𝔠] = [x=>x.start.line,x=>x.start.character];
  let 𝔫 = ([x,...y])=>[+x,...y]
  let S = 𝒪ℒ(𝐸.selections.G(𝔩)).ᴍ(𝔫)
          .s(x=>x[0])
          .ꟿ((l,C)=>[l,C.s(𝔠)]);
  let X = S.ꟿ((l,C)=>[l,C.ᴍ(𝔠)]);
  let N = getSpacing(X);
  𝐸.edit(𝑒𝑏=>ζ(N.ζ()[1],S.ζ()[1]).ᴍ(x=>x.ζ())
             .flat().ꟿ((c,s) => 𝑒𝑏.replace(s,' '.repeat(c)))); };
align.manual = true;

const dirOpener = 𝐸 => { 
    const fdir = 𝐸?.document.uri.fsPath ?path.dirname(𝐸.document.uri.fsPath): null;
    const wdir = vs.workspace.workspaceFolders?.[0]?.uri.fsPath || '.';
    exec(`forgor term --working-directory "${fdir || wdir}"`); };
dirOpener.manual = true;

const fileRun = 𝐸 => {
    const fpat = 𝐸.document.uri.fsPath;
    exec(`forgor extrunner "${fpat}"`); };
fileRun.manual = true;

const wall = 𝐸 => {
    𝐸.selections = 𝐸.selections.ᴍ(𝔖𝔏)
                    .ᴍ(([αl,αc,βl,βc]) => [𝔏𝔖(αl,αc,αl,αc),𝔏𝔖(βl,βc,βl,βc)])
                    .flat(1); };
wall.manual = true;

const splitLineKeepCol = 𝐸 => {
  if(!𝐸) return;
  const P = [];
  𝐸.edit(𝑒𝑏 =>
    𝐸.selections.forEach(sel => {
      const l = sel.active.line;
      const c = sel.active.character;
      const lineText = 𝐸.document.lineAt(l).text;
      const [before,after] = [lineText.slice(0,c),lineText.slice(c)];
      const txt = `\n${' '.repeat(ᔐ𝑙(before))}`; //${after}\n`;
      𝑒𝑏.replace(sel,txt); })); };
splitLineKeepCol.manual = true;

// 􀁗􀊩􀗁􀝍􀩥􁁨􁊺
const tools = { sup  : s=>[...s].ᴍ(c=>SUP[c]??c).join(''),
                sub  : s=>[...s].ᴍ(c=>SUB[c]??c).join(''),
                nrm  : s=>[...s].ᴍ(c=>NRM[c]??c).join(''),
                ord1 : s=>mapS(s, 1,  1),
                dro1 : s=>mapS(s,-1,  1),
                ord3 : s=>mapS(s, 3,  1),
                dro3 : s=>mapS(s,-3,  1),
                set0 : s=>mapS(s, 0,- 0),
                set3 : s=>mapS(s, 0,- 3),
                set7 : s=>mapS(s, 0,- 7),
                set9 : s=>mapS(s, 0,- 9),
                set13: s=>mapS(s, 0,-13),
                set16: s=>mapS(s, 0,-16),
                set19: s=>mapS(s, 0,-19),
                wall, align, dirOpener, fileRun, splitLineKeepCol }
// 󰤱 generalized upper/lower/swapcase, switching alphabets

const fc = (𝐸,l,c) => [l,ᔐ𝑙(part(    𝐸.document.lineAt(l).text, c)[0])               ];
const cf = (𝐸,l,c) => [l,   part([...𝐸.document.lineAt(l).text],c)[0].join('').length];
const tin = (𝐸,𝚜,ƒ) => { 𝚜 = ƒ( [...fc(𝐸,𝚜[0],𝚜[1]),...fc(𝐸,𝚜[2],𝚜[3])]);
                         return [...cf(𝐸,𝚜[0],𝚜[1]),...cf(𝐸,𝚜[2],𝚜[3]) ]; }
const a1 = (𝐸,𝚜) => tin(𝐸,𝚜,𝚜=>[𝚜[0],𝚜[1],𝚜[2],𝚜[3]+1]);
const nzSel = (𝐸,𝚜) => (𝚜=>𝔏𝔖(...𝚜[0]==𝚜[2]&&𝚜[1]==𝚜[3] ?a1(𝐸,𝚜): [𝚜[0],𝚜[1],𝚜[2],𝚜[3]]))(𝔖𝔏(𝚜));

const activateHighlighter = ℭ => {
    const updateDecorations = 𝐸 => {
        if(!𝐸) return;
        const text = 𝐸.document.getText();
        for(const [R,S] of highlights) {
            const locs = [];
            let m;
            while((m = R.exec(text))) {
                const [s,e] = [m.index,m.index+m[0].length].ᴍ(𝐸.document.positionAt);
                locs.push({ range: new vs.Range(s,e) }); }
            𝐸.setDecorations(S,locs); } };
    const activeEditor = vs.window.activeTextEditor;
    if(activeEditor) updateDecorations(activeEditor);
    vs.window.onDidChangeActiveTextEditor(updateDecorations, null, ℭ.subscriptions);
    vs.workspace.onDidChangeTextDocument(ε => {
        const 𝐸 = vs.window.activeTextEditor;
        if(𝐸 && ε.document === 𝐸.document) updateDecorations(𝐸);
    }, null, ℭ.subscriptions); };

const activateSelectionTools = ℭ => {
    𝒪ℒ(tools).ᴍ(([k,v])=>
        vs.commands.registerCommand(`moon.${k}`, _=>{
            const 𝐸 = vs.window.activeTextEditor;
            if(v.manual) v(𝐸);
            else         𝐸.edit(𝑒𝑏 => 𝐸.selections.ᴍ(𝚜 => nzSel(𝐸,𝚜))
                                       .forEach(𝚜 => 𝑒𝑏.replace(𝚜,v(𝐸.document.getText(𝚜))))); })
    ).forEach(ℭ.subscriptions.push); };

const activate = ℭ => { activateHighlighter(ℭ); activateSelectionTools(ℭ); }
const deactivate = _ => {};

module.exports = { activate, deactivate };