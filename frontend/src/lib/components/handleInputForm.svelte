<script lang="ts">
    import { goto } from '$app/navigation';
    let handle = $state('');
    async function handleSubmit(event: SubmitEvent) {
        event.preventDefault()
        const response = await fetch('http://localhost:8000/api/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ handle })
        });
        if (response.ok) {
            goto('/');
}
    }
</script>
	


<form onsubmit={handleSubmit}>

    <div id="handleInput">
        <label for="handle">CF hanlde</label>
        <input id="handletext" type="text" bind:value={handle}/>
    </div>

    <button type="submit">Submit</button>


</form>