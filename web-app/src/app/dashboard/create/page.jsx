import Link from 'next/link'
import React from 'react'
const Page = () => {
  return (
    <div className='h-screen pt-20 px-4 pb-4 space-y-3 overflow-auto'>
        <form className='space-y-3' action="">
            <h1 className='font-bold text-3xl'>Submit your application</h1>
            <div className='space-y-3'>
                <label className='sm:flex sm:items-center space-y-3 sm:space-y-0'>
                    <span className='w-1/4'>App Name</span>
                    <input className='input input-block' type="text" />
                </label>
                <label className='sm:flex sm:items-center space-y-3 sm:space-y-0'>
                    <span className='w-1/4'>App description</span>
                    <input className='input input-block' type="text" />
                </label>
                <label className='sm:flex sm:items-center space-y-3 sm:space-y-0'>
                    <span className='w-1/4'>App website</span>
                    <input className='input input-block' type="text" />
                </label>
                <label className='sm:flex sm:items-center space-y-3 sm:space-y-0'>
                    <span className='w-1/4'>Redirect URI</span>
                    <input className='input input-block' type="text" />
                </label>
                <label className='sm:flex sm:items-center space-y-3 sm:space-y-0'>
                    <span className='w-1/4'>App type</span>
                    <input className='input input-block' type="text" />
                </label>
                <label className='sm:flex sm:items-center space-y-3 sm:space-y-0'>
                    <span className='w-1/4'>App role</span>
                    <input className='input input-block' type="text" />
                </label>
                <label className='sm:flex sm:items-center space-y-3 sm:space-y-0'>
                    <span className='w-1/4'>App scopes</span>
                    <input className='input input-block' type="text" />
                </label>
            </div>
            <p className='sm:text-center'>Terms of services</p>
            <div className='flex gap-3 sm:justify-center'>
                <button type='submit' className='btn btn-primary'>Create application</button>
                <Link href={'/dashboard/'} className='btn btn-outline-secondary'>Cancel</Link>
            </div>
        </form>
    </div>
  )
}

export default Page