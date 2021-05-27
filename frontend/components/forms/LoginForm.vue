<template>
    <div>
        <form method="post">
            <b-field>
                <template #label>
                    <span class="has-text-white">Email</span>
                </template>
                <b-input type="email" icon="email" placeholder="john@doe.com">
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
    </div>
</template>

<script>
export default {
    name: "LoginForm",
};
</script>

<style lang="scss" scoped>
.button {
    background-color: $primary;
}
</style>