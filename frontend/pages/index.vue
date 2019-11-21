<template>
  <div>
    <post v-for="post in posts" :key="post.id" :post="post" class="mb-4"></post>
  </div>
</template>

<script>

export default {

  async asyncData ({ app }) {
    try {
      const response = await app.$axios.get('/api/posts/')
      return {
        posts: response.data.results,
        error: false
      }
    } catch (e) {
      console.log('error', e)
      return {
        posts: [],
        error: true
      }
    }
  }
}

</script>

<style>

</style>
