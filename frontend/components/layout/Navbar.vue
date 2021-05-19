<template>
    <div>
        <nav
            class="navbar is-dogeblueprimary"
            role="navigation"
            aria-label="main navigation"
        >
            <div class="navbar-brand">
                <a class="navbar-item" href="https://bulma.io">
                    <img
                        src="https://bulma.io/images/bulma-logo-white.png"
                        width="112"
                        height="28"
                    />
                </a>

                <a
                    role="button"
                    class="navbar-burger"
                    aria-label="menu"
                    aria-expanded="false"
                    data-target="navbarBasicExample"
                >
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </a>
            </div>

            <div id="navbarBasicExample" class="navbar-menu">
                <div class="navbar-end" v-if="$auth.loggedIn">
                    <div class="navbar-item">
                        <div class="field is-grouped">
                            <div class="navbar-item has-dropdown is-hoverable">
                                <a class="button is-primary is-outlined">
                                    <span>Account</span>
                                </a>

                                <div class="navbar-dropdown is-right is-boxed">
                                    <a class="navbar-item">
                                        {{ $auth.user.email }}
                                    </a>
                                    <hr class="navbar-divider" />
                                    <a class="navbar-item"> Profile </a>
                                    <a class="navbar-item" href="">
                                        Reset password
                                    </a>
                                    <hr class="navbar-divider" />
                                    <a class="navbar-item" href=""> Log out </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- username -->
                    <!-- logout button -->
                </div>
                <div class="navbar-end" v-else>
                    <div class="navbar-item">
                        <div class="buttons">
                            <a class="button is-primary is-outlined">
                                Log in
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    name: "Navbar",
};
</script>

<style lang="scss" scoped>
</style>
