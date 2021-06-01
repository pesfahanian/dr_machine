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

                <LoginForm />

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
        <Footer />
    </section>
</template>

<script>
import LoginForm from "@/components/forms/LoginForm";
import Footer from "@/components/layout/Footer";

export default {
    layout: "bare",
    components: {
        LoginForm,
        Footer,
    },
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
