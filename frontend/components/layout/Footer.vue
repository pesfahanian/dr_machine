<template>
    <div>
        <footer class="footer is-primary">
            <div class="content has-text-centered has-text-light">
                <p>
                    Copyright 2021 <strong class="has-text-primary">Dr. Machine</strong>. All rights reserved.
                </p>
            </div>
        </footer>
    </div>
</template>

<script>
    export default {
        name: "Footer",
    };
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/style.scss";

    .footer {
        background-color: $dogeblueprimary;
    }
</style>
