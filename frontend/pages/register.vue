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

                <RegisterForm />

                <hr />
                <nav class="level">
                    <div class="level-item has-text-centered">
                        <div>
                            <h1 class="has-text-light">
                                Already have an account?
                                <NuxtLink to="/login">Log in</NuxtLink>
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
import RegisterForm from "@/components/forms/RegisterForm";
import Footer from "@/components/layout/Footer";

export default {
    layout: "bare",
    components: {
        RegisterForm,
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
