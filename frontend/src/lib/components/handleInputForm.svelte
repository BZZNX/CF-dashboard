
<script>
    let name = $state();
    let handle = $state();
</script>
	


<form>
    <div id="nameInput">
        <label for="name">Name</label>
        <input id="nametext" type="text" bind:value={name}/>
    </div>

    <div id="handleInput">
        <label for="handle">CF hanlde</label>
        <input id="handletext" type="text" bind:value={handle}/>
    </div>

    <button id="submit">Submit</button>


</form>