<script lang="ts">
    import { fetchPublic } from "$lib/api";
    import { onMount } from "svelte";

    type HealthResponse = { status: string }; 
    
    let backendStatus = $state("Wird geladen...");

    onMount(async () => {
        try {
            const res = await fetchPublic<HealthResponse>("/health");
            backendStatus = res.status; 
        } catch (error) {
            backendStatus = "Fehler bei der Verbindung";
        }
    });
</script>

<h1>Status of Backend: {backendStatus}</h1>