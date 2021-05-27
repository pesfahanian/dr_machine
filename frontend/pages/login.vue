<template>
    <section class="hero is-fullheight">
        <div class="hero-body">
            <div class="login">
                <div class="has-text-centered">
                    <NuxtLink to="/">
                        <img
                            src="https://bulma.io/images/bulma-logo-white.png"
                            width="300px"
                        />
                    </NuxtLink>
                </div>

                <hr />

                <form method="post">
                    <b-field>
                        <template #label>
                            <span class="has-text-white">Email</span>
                        </template>
                        <b-input
                            type="email"
                            icon="email"
                            placeholder="john@doe.com"
                        >
                        </b-input>
                    </b-field>
                    <b-field>
                        <template #label>
                            <span class="has-text-white">Password</span>
                        </template>
                        <b-input
                            type="password"
                            icon="key-variant"
                            placeholder="************"
                            password-reveal
                        >
                        </b-input>
                    </b-field>

                    <br />

                    <button
                        class="button is-block is-fullwidth is-primary is-medium"
                        type="submit"
                    >
                        Log in
                    </button>
                </form>

                <br />

                <nav class="level">
                    <div class="level-item has-text-centered">
                        <div>
                            <NuxtLink to="">Forgot password?</NuxtLink>
                        </div>
                    </div>
                </nav>
                <hr />
                <nav class="level">
                    <div class="level-item has-text-centered">
                        <div>
                            <h1 class="has-text-light">
                                Don't have an account?
                                <NuxtLink to="/register">Register</NuxtLink>
                            </h1>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    layout: "bare",
};
</script>

<style lang="scss" scoped>

.hero {
    background-color: $dogeblueprimary;
}

.hero-body {
    justify-content: center;
}

.login {
    border-radius: 25px;
    padding: 1.5rem;
    box-shadow: 8px 8px 15px #151a21, -8px -8px 15px #1b2430;
}

</style>
