class ApiClient {
    constructor(baseUrl) {
      this.baseUrl = baseUrl;
    }
  
    async get(endpoint) {
      const response = await fetch(`${this.baseUrl}/${endpoint}`);
      return response.json();
    }
  
    async post(endpoint, data) {
      const response = await fetch(`${this.baseUrl}/${endpoint}`, {
        method: 'POST',
        body: JSON.stringify(data)
      });
      return response.json();
    }
  }
  
  // Использование
  const api = new ApiClient('https://api.example.com');
  api.get('users').then(users => console.log(users));
