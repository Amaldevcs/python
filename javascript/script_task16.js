function printBoard(){
size = 8;
var partial = [1,2,3,4,5,6,7,8];
for(i=0;i<partial.length;++i){
col = partial[i];
dot = "";
for (i=0;i<col-1;++i){
dot=dot+".";
}
dot = dot +"Q";
//console.log(dot);
pot = "";
for(j=0;j<size-col;++j){
pot =pot +".";
}
got = dot+pot;
console.log(got); 
}
}
printBoard();

