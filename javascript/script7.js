function frequency(str){
freq = {};
for (i=0;i<str.length;++i){
var a =0;
for (j= 0;j<str.length;++j){
if(str[i] === str[j]){
a++;}
freq[str[i]] = a;
}
}
return freq;
}
freqs = frequency("aaabbcdee");
console.log(freqs);
function sortfreq(freqs){
keys = Object.keys(freqs);
tuples = [];
for(i=0;i<keys.length;++i){
tuples.push([freqs[keys[i]],keys[i]]);
}
tuples.sort()
return tuples
}
tuples = sortfreq(freqs);
console.log(tuples);
//least = ();
//rest = [];
function tree(tuples){
while(tuples.length>1){
least = [];
rest = [];
for(i=0;i<2;++i){
least.push(tuples[i]);}
//console.log(least);
for(i=2;i<tuples.length;++i){
rest.push(tuples[i]);}
//console.log(rest);
comb = least[0][0] + least[1][0];
tuples = [];
rest.push([[comb,least]]);
tuples.push(rest);
tuples.sort();
}
//return tuples[0];
}
tree(tuples);
function trim(tree){
p = tree[1];
if (typeof(p) === typeof("")){
return p;}else{return (trim(p[0]),trim(p[1]));}
}
tt = trim(tuples[0]);
codes = {}
function assign(node,pat=''){
if(typeof(node) === typeof(""){codes[node]=pat;}else{
assign(node[0],pat,+"0");
assign(node[1],pat+"1");
}
}
assign(tt);
console.log(codes)
