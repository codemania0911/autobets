      <template>
        <div class="mt-2">
          <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse is-nav id="nav-collapse">

              <b-navbar-nav>
                <b-nav-item to="/events">Events</b-nav-item>
                <b-nav-item to="/monitor">Monitor</b-nav-item>
                <b-nav-item to="/configuration">Configuration</b-nav-item>
                <b-nav-item to="/reports">Reports</b-nav-item>

              </b-navbar-nav>

              <b-navbar-nav class="ml-auto" v-if="$store.state.loggedIn">
                <b-nav-text>{{ $store.state.user.username }}</b-nav-text>
                
                <b-nav-item @click.prevent="logout()">Logout</b-nav-item>
              </b-navbar-nav>

              <b-navbar-nav class="ml-auto" v-if="!$store.state.loggedIn">
                <b-nav-item to="/login">Login</b-nav-item>
              </b-navbar-nav>
            </b-collapse>
          </b-navbar>
          <div class="mt-2">
            <nuxt/>
            
          </div>
        </div>
      </template>

      <script>

      export default {
      

      
      methods: {
          logout () {
            this.$store.dispatch('logout')
            this.$router.push('/')
          }
        }
      }
      </script>

      <style>



      </style>
