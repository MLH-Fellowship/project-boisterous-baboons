// Fetchong posts from API

var posts;

fetch("/api/timeline_post")
    .then((response) => {
    if (response.ok) {
        return response.json();
    } else {
        throw new Error("NETWORK RESPONSE ERROR");
    }
    })
    .then(data => {
    console.log(data.timeline_posts);
    posts = data.timeline_posts;
    initPostList(posts);
    })
    .catch((error) => console.error("FETCH ERROR:", error));


    // Sequence to create cards for each post
let cardContainer;

let createPostCard = (post) => {
    let card =  document.createElement('div');
    card.className = 'card w-75'; 
    
    let cardBody = document.createElement('div');
    cardBody.className = 'card-body';

    let title = document.createElement('h5');
    title.innerText = post.name;
    title.className = 'card-title';

    let content = document.createElement('p');
    content.className = 'card-text';
    content.innerText = post.content;

    cardBody.appendChild(title);
    cardBody.appendChild(content);
    card.appendChild(cardBody);
    cardContainer.appendChild(card);
}


let initPostList = () => {
    if (cardContainer) {
        document.getElementById('card-container').replaceWith(cardContainer);
        return;
    }

    cardContainer = document.getElementById('card-container');
    posts.forEach((post) => {
        createPostCard(post);
    });
    
};

//initPostList();