<template>
  <div class="mycontainer">
    <div>
      <logo />
      <!-- <h1 class="title">
        CFL Tools
      </h1>
      <h2 class="subtitle">
        Center for Financial Literacy Tools
      </h2> -->
      <div class="links" style="margin-top: 25px;">
        <nuxt-link to="/loans" style="margin-bottom: 24px;"
          class="button--green"
        >
          Student Loan Calculator
        </nuxt-link>
        <a
          href="mailto:grplyler@liberty.edu"
          target="_blank"
          class="button--grey" style="margin-bottom: 24px;"
        >
          Contact
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'

export default {
  components: {
    Logo
  }
}
</script>

<style scoped>
.mycontainer {
  margin: 0 auto;
  padding: 24px;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
