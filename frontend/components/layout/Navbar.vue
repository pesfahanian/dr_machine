<template>
	<b-navbar>
		<template #brand>
			<b-navbar-item tag="router-link" :to="{ path: '/' }">
				<img
					src="https://bulma.io/images/bulma-logo-white.png"
					alt="Dr. Machine. Intelligent Medical Imaging."
				/>
			</b-navbar-item>
		</template>

		<template #end>
			<b-navbar-item tag="div">
				<div class="buttons">
					<NuxtLink class="button is-primary is-outlined" to="/login"
						>Log in</NuxtLink
					>
				</div>
			</b-navbar-item>
		</template>
	</b-navbar>
</template>

<script>
export default {
	name: "Navbar",
};
</script>

<style lang="scss" scoped>
.navbar {
	background-color: $dogeblueprimary;
}

.navbar-menu .is-active {
	background-color: lighten($color: $dogeblueprimary, $amount: 10) !important;
}
</style>
