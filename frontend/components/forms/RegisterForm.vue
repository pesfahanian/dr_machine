<template>
	<div>
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
					<span class="has-text-white">Mobile</span>
				</template>
				<b-input
					icon="phone"
					placeholder="+989xxxxxxxxx"
				>
				</b-input>
			</b-field>

            <b-field>
				<template #label>
					<span class="has-text-white">National ID</span>
				</template>
				<b-input
					icon="credit-card"
					placeholder="xxxxxxxxxxx"
				>
				</b-input>
			</b-field>

			<br />

			<button
				class="button is-block is-fullwidth is-primary is-medium"
				type="submit"
			>
				Submit
			</button>
		</form>
	</div>
</template>

<script>
export default {
	name: "RegisterForm",
};
</script>

<style lang="scss" scoped>
.button {
	background-color: $primary;
}
</style>
