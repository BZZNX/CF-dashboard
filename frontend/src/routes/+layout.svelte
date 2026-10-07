<script lang="ts">
	import Navbar from '$lib/components/navbar.svelte';
	import { onMount } from 'svelte';

	type CFUser = {
        handle: string;
        rating: number | null;
        maxRating: number | null;
    };

	let users = $state([]);
	
	async function loadUsers() {
			const response = await fetch('http://localhost:8000/api/users');
			users = await response.json();
		}
	onMount( () => {
		loadUsers();
	});

</script>



<Navbar />
<table>
    <caption>Global CF ranking</caption>
    <thead>
        <tr>
            <th scope="col">Position</th>
            <th scope="col">Handle</th>
            <th scope="col">Rating</th>
            <th scope="col">Max Rating</th>
        </tr>
    </thead>
    <tbody>
		{#each users as user, index}
			<tr>
				<td>{index + 1}</td>
				<td>{user["handle"]}</td>
				<td>{user["rating"]}</td>
				<td>{user["maxRating"]}</td>
			</tr>
		{/each}
    </tbody>
    
</table>


