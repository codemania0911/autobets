      <template>
              <div class="container">
                <span>Balance</span>
                <ul class="trendings">
                  <li v-for="bal in balance" 
                      :key="bal.id">

                    <span>{{ bal.balance }}</span>

                  </li>

                </ul>
              </div>
            </template>

      <script>

      export default {
          data: () => ({ balance: [] }),
          
          async asyncData ({ app }) {
        
          try {
            const response = await app.$axios.get('/api/balance/')

            return {
              balance: response.data.results,

              error: false
            }
          } catch (e) {
            console.log('error', e)

          }
        
        },  
      };

      </script>

      <style>

      container {
      font-family: ‘Lato’, sans-serif;
      font-size: 12px;
      font-weight: 400;
      padding: 10px;
      text-align: left;
      width: -20%;
      }
      </style>