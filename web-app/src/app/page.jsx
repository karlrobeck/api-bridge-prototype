"use client";
import { redirect } from "next/navigation";
import { useEffect } from "react"

export default function Home() {

  useEffect(() => {
    redirect(`
    /auth/login?client_id=${process.env.NEXT_PUBLIC_CLIENT_GATEWAY_API_CLIENT_ID}&response_type=code&redirect_uri=http://localhost:3000/auth/callback&state=&show_dialog=false&scope=
    `)
  },[])

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      test
    </main>
  )
}
