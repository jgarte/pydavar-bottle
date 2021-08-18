function trans(string){

	        let letters_he = "אבגדהוזחטיכלמנסעפצקרשת"+" ־"+"׳"+'״'
	        let letters_la = "xbgdhvzHTjklmnsypcqrwt"+" -"+"'"+'"'
	        
	        let concatenated = letters_he.concat(letters_la).concat(" ")
	        
	        let trimmer = RegExp("[^"+concatenated+"]", "g")

	        for(let i in letters_he){
			                x = letters_he[i];
			                y = letters_la[i];

			                r = new RegExp(y, 'g');

			                string = string.replace(r, x);

			        }

	        return string.replace(trimmer, "")
}


function init(){
	let input = document.getElementById("search");
	input.addEventListener('keypress', () => {input.value = trans(input.value)});
	input.addEventListener('keydown', () => {input.value = trans(input.value)});
	input.addEventListener('keyup', () => {input.value = trans(input.value)});
}
