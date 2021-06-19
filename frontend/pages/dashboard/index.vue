<template>
    <div>
        <Navbar />
        <section class="hero is-fullheight">
            <div class="hero-body">
                <section class="section">
                    <div class="columns">
                        <div class="column is-10 is-offset-1">
                            <div class="container has-text-centered is-fluid">
                                <div class="hero is-light">
                                    <div class="hero-body">
                                        <h2 class="title is-4">
                                            Sign up for our newsletter
                                        </h2>
                                        <div class="column is-6 is-offset-3">
                                            <div
                                                class="
                                                    field
                                                    has-addons
                                                    has-addons-centered
                                                "
                                            >
                                                <div
                                                    class="control is-expanded"
                                                >
                                                    <input
                                                        class="input"
                                                        type="text"
                                                        placeholder="Email address"
                                                    />
                                                </div>
                                                <div class="control">
                                                    <a class="button is-info">
                                                        Subscribe
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
            <Footer />
        </section>
    </div>
</template>

<script>
import LoginForm from "@/components/forms/LoginForm";
import Footer from "@/components/layout/Footer";
import Navbar from "@/components/layout/Navbar";

export default {
    layout: "bare",
    components: {
        LoginForm,
        Navbar,
        Footer,
    },
};
</script>

<style lang="scss" scoped>
.navbar {
    background-color: $dogeblueprimary;
}

.hero-body {
    justify-content: center;
}
</style>
