import React from 'react'

const Page = () => {
  return (
    <div className='h-screen pt-20 px-4 pb-4 space-y-3 overflow-auto'>
        <p>Base template</p>
        <h1 className='text-5xl font-bold'>
            HOME DASHBOARD
        </h1>
        <div className='card max-w-full'>
            <div className='card-body'>
                Application 1
            </div>
        </div>
        <div className='card max-w-full'>
            <div className='card-body'>
                Application 2
            </div>
        </div>
        <div className='card max-w-full'>
            <div className='card-body'>
                Application 3
            </div>
        </div>
    </div>
  )
}

export default Page