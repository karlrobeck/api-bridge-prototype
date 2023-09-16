"use client";
import React, { useEffect } from 'react'
import { redirect, useSearchParams } from 'next/navigation'

const Page = () => {

    const query = useSearchParams()

    useEffect(() => {

        const get_token = async () => {
            const res = await fetch('http://localhost:8000/v1/security/token',{
                method:'POST',
                headers:{
                    'encoded-data':'Basic ' + (new Buffer.from(process.env.NEXT_PUBLIC_CLIENT_GATEWAY_API_CLIENT_ID + ':' + process.env.NEXT_PUBLIC_CLIENT_GATEWAY_API_CLIENT_SECRET).toString('base64')),
                    'Content-type':'application/json',
                },
                body:JSON.stringify({
                    code:query.get('code'),
                    redirect_uri:'http://localhost:3000/auth/callback',
                    grant_type:'authorization_code'
                })})
            if (!res.ok){
                redirect('auth/login')
            }
            const data = await res.json()
            window.localStorage.setItem('sentinel_access_token',data.access_token)
            window.localStorage.setItem('sentinel_token_type',data.token_type)
            window.localStorage.setItem('sentinel_scope',data.scope)
            window.localStorage.setItem('sentinel_expires_in',data.expires_in)
            window.localStorage.setItem('sentinel_refresh_token',data.refresh_token)
        }
        get_token()
        redirect('/dashboard')
    },[])

  return (
    <div>Callback function</div>
  )
}

export default Page