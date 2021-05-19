<template>
    <div>
        <section class="hero is-dogeblueprimary is-fullheight">
            <div class="hero-head">
                <Navbar />
            </div>

            <div class="hero-body">
                <div class="container has-text-centered">
                    <p class="title">Dr. Machine</p>
                    <p class="subtitle has-text-grey">
                        Intelligent Medical Imaging
                    </p>
                </div>
            </div>

            <!-- Hero footer: will stick at the bottom -->
            <div class="hero-foot">
                <nav class="tabs is-boxed is-fullwidth">
                    <div class="container">
                        <ul>
                            <li
                                v-bind:class="{ 'is-active': isActive == 'intro' }"
                                v-on:click="
                                    isActive = 'intro';
                                    scroll('intro');
                                "
                            >
                                <a class="has-text-primary">Introduction</a>
                            </li>
                            <li
                                v-bind:class="{ 'is-active': isActive == 'service' }"
                                v-on:click="
                                    isActive = 'service';
                                    scroll('service');
                                "
                            >
                                <a class="has-text-primary">Services</a>
                            </li>
                            <li
                                v-bind:class="{ 'is-active': isActive == 'team' }"
                                @click="
                                    isActive = 'team';
                                    scroll('team');
                                "
                            >
                                <a class="has-text-primary">Team</a>
                            </li>
                            <li
                                v-bind:class="{ 'is-active': isActive == 'contact' }"
                                @click="
                                    isActive = 'contact';
                                    scroll('contact');
                                "
                            >
                                <a class="has-text-primary">Contact</a>
                            </li>
                        </ul>
                    </div>
                </nav>
            </div>
        </section>
        <section>
            <div class="content">
                <div ref="intro" v-show="isActive == 'intro'">My Introduction</div>
                <div ref="service" v-show="isActive == 'service'">My Services</div>
                <div ref="team" v-show="isActive == 'team'">My Team</div>
                <div ref="contact" v-show="isActive == 'contact'">My Contact</div>
            </div>
        </section>
    </div>
</template>

<script>
import Navbar from "@/components/layout/Navbar";

export default {
    layout: "just_footer",
    components: {
        Navbar,
    },
    data() {
        return {
            isActive: "intro",
        };
    },
    methods: {
        scroll(refName) {
            var element = this.$refs[refName];
            var top = element.offsetTop;

            window.scrollTo(0, top);
        },
    },
};
</script>

<style lang="scss" scoped>
</style>
