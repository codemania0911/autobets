<template>
    <div>
        
    </div>
</template>

<script>
import axios from 'axios';
export default { 
    created: function (){
       const response = axios.get('/api/events');
    return {
        events: response.data.results,
        error: false
      }    
    return{ 
    events : [], 
    }
    },
    }
</script>