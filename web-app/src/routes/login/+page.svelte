<script>
    const redirect_to_app = (event) => {
        document.getElementById('main_image').style.width = "0%"
        document.getElementById('signin_form').style.opacity = "0%"
        document.getElementById('signin_form').style.width = "100%"
        document.getElementById('loading_screen').style.opacity = "100%"
        document.getElementById('loading_screen').style.visibility = "visible"

        document.getElementById('loading_text').innerText = 'Authenticating'
        
        setTimeout(() => {
            document.getElementById('loading_text').innerText = 'Redirecting...'
        }, 1000);
    }
</script>
<main class="flex dark:bg-gray-700">
    <div id="loading_screen" class="space-x-3 absolute inset-0 opacity-0 invisible flex transition-all duration-700 justify-center items-center">
        <div class="animate-spin inline-block w-6 h-6 border-[3px] border-current border-t-transparent text-gray-800 rounded-full dark:text-white" role="status" aria-label="loading">
            <span class="sr-only">Loading...</span>
        </div>
        <h1 id="loading_text" class="dark:text-white text-2xl font-bold">Loading System</h1>
    </div>
    <form on:submit|preventDefault={redirect_to_app} id="signin_form" class="min-h-screen transition-all duration-700 sm:w-1/4 w-full max-w-full px-8 py-8 flex flex-col justify-between" action="">
        <div class="space-y-3">
            <div class="flex flex-col items-center gap-3">
                <img class="w-16 pb-5" src="Sti_logo.png" alt=""> 
                <h1 class="text-center font-bold text-3xl dark:text-white">Sign In</h1>
                <input placeholder="Username" class="py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400" type="text">
                <input placeholder="Password" class="py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400" type="text">
            </div>
            <div class="flex">
                <input type="checkbox" class="shrink-0 mt-0.5 border-gray-200 rounded text-blue-600 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:checked:bg-blue-500 dark:checked:border-blue-500 dark:focus:ring-offset-gray-800" id="hs-checkbox-group-1">
                <label for="hs-checkbox-group-1" class="text-sm text-gray-500 ml-3 dark:text-gray-400">
                    Remember me
                </label>
            </div>
        </div>
        <button type="submit" class=" w-full py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border border-transparent font-semibold bg-blue-500 text-white hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all text-sm dark:focus:ring-offset-gray-800">
            Sign in
        </button>
    </form>
    <img id="main_image" class="transition-all duration-700 object-cover sm:w-3/4 hidden sm:block max-w-fit" src="sti_image.jpg" alt="">
</main>
