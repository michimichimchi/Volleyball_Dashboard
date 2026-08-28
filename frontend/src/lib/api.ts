const API_BASE = 'http://localhost:8000';


export async function fetchPublic<T>(path: string): Promise<T> {
	const res = await fetch(`${API_BASE}${path}`);
	if (!res.ok) throw new Error("Fehler beim Abrufen der öffentlichen Daten");
	return res.json();  
}