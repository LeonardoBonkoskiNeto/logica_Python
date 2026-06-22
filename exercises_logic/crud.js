console.log('hello people'); 
console.log('#buildingCRUDS');
    
//[CRUD] Javascript basico
const miniTwitter = {
    users:[
        {
            username: 'leonardo',
        }
    ],
  posts: [
    {   
    
        owner: 'leonardo',
        Content: 'my first tweet',
    }
    ],
 };

//CREAT
function creatPost(data) {
    miniTwitter.posts.push ({
        id: miniTwitter.posts.length + 1,
        owner: data.owner,
        content: data.content
    });
}
creatPost({owner: 'leonardo', content: 'seccond tweet'});
creatPost({owner: 'leonardo', content: 'third tweet'});
console.log(miniTwitter.posts)
//READ
function pegaPosts() {
    return miniTwitter.posts;
}
console.log(pegaPosts()) 
//UPDATE
function atualizaContentDoPost(id, novoConteudo) {
    const postQueVaiSerAtualizado = pegaPosts().find((post) => {
          return post.id === id;
    });
    console.log(postQueVaiSerAtualizado)
    postQueVaiSerAtualizado.content = novoConteudo 
}
atualizaContentDoPost(1, 'new content of post')
console.log(pegaPosts())

//DELETE
function apagaPost(id) {
  const listaDePostsAtualizada = pegaPosts().find((posts) => {

  } )
  miniTwitter.posts = listaDePostsAtualizada; 

  }

