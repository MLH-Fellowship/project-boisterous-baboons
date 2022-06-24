const form = document.getElementById('post-form');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const payload = new FormData(form);

        fetch('/api/timeline_post', {
            method: 'POST',
            body:payload,
        })
        .then(res => res.json())
        .then(data => console.log(data))
        form.reset();
    })